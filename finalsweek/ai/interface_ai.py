from game.configuration.definitions import PhaseTypeName
from game.configuration.settings import generation
from game.gameflow.actions.action_card import ActionCardAction
from game.gameflow.actions.base import ActionBase
from logger import log


class AiActor(object):
    def __init__(self, _id, game_id, interface) -> None:
        super().__init__()
        self.game_id = game_id
        self.interface = interface
        self.id = _id
        self.prompt_card_map = dict()

    def take_turn_if_possible(self):
        digest = self.__get_game_info()
        if self.__is_it_my_turn(digest):
            log("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            self.__think("Starting new turn for actor: {}".format(self.id))
        while True:
            if digest.complete:
                return
            if not self.__is_it_my_turn(digest):
                return digest.turn.current_turn_actor_id
            old_turn_id = digest.turn.id
            action = self.__get_action(digest)
            if not action:
                del self.prompt_card_map[digest.turn.prompt.id]
                digest = self.__get_game_info(fresh=True)
                continue
            digest = self.__commit_action(digest, action)
            if digest.complete:
                return
            if digest.turn.id != old_turn_id and digest.turn.current_turn_actor_id != self.id:
                self.__think("My turn is complete!")
                return digest.turn.current_turn_actor_id

    def __commit_action(self, digest, action):
        return self.interface.take_turn(
            game_id=self.game_id,
            requesting_actor_id=self.id,
            action=action)

    def __get_game_info(self, fresh=False):
        return self.interface.load(self.game_id, self.id, fresh=fresh)

    def __is_it_my_turn(self, digest):
        return not digest.complete and digest.turn and digest.turn.current_turn_actor_id == self.id

    def __get_action(self, digest):
        turn = digest.turn
        if turn.phase_type != PhaseTypeName.Classtime:
            return ActionBase()
        return self.__build_classtime_action(digest)

    def __build_classtime_action(self, digest):
        # cards in play:
        cards_in_play = digest.in_play_effects.cards_in_play
        cards_in_play_names = ", ".join(["'{}'".format(c.template.name) for c in cards_in_play])
        self.__think("My cards in play: {}".format(cards_in_play_names))

        turn = digest.turn
        card_id = self.__get_card_id(turn)
        prompt = turn.prompt
        for answer_key, prompt_options in prompt.pending:
            self.__enumerate_options(answer_key, prompt_options)
            if not prompt_options:
                self.__think("Skipping prompt", prompt.id, "for card", card_id, "... no options")
                self.__set_card_prompt_map(prompt.id, None)
                return
            selection = generation["random"].choice([o["id"] for o in prompt_options])
            prompt.answer(answer_key, selection)
        return ActionCardAction(card_id, prompt)

    def __enumerate_options(self, answer_key, prompt_options):
        self.__think("> Have a decision to make, '{}':".format(answer_key))
        for option in prompt_options:
            self.__think("   {}: {}".format(option["display"], option["id"]))

    def __get_card_id(self, turn):
        card_id = self.prompt_card_map.get(turn.prompt.id, False) or self.__choose_card(turn)
        self.__set_card_prompt_map(card_id, turn.prompt.id)
        return card_id

    def __set_card_prompt_map(self, card_id, prompt_id):
        self.prompt_card_map[prompt_id] = card_id

    def __choose_card(self, turn):
        hand = turn.hand.action_cards
        card_names = ", ".join(["'{}'".format(c.template.name) for c in hand])
        self.__think("My hand: {}".format(card_names))
        card_id = generation["random"].choice([ac.id for ac in turn.hand.action_cards])
        self.__think("I choose card:", self.__get_card_details(card_id, turn))
        return card_id

    @staticmethod
    def __think(*a):
        log(">", *a)

    @staticmethod
    def __get_card_details(card_id, turn):
        for card in turn.hand.action_cards:
            if card.id == card_id:
                return "{}".format(card.template.name)
