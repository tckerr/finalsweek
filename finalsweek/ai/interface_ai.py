from trace.definitions import LogLevel, LogType
from trace.logger import Logger
from util.random import choice


class AiActor(object):
    def __init__(self, _id, game_id, label, api_client) -> None:
        super().__init__()
        self.game_id = game_id
        self.id = _id
        self.label = label
        self.prompt_card_map = dict()
        self.api_client = api_client

    def take_turn_if_possible(self):
        data = self.__get_game_info()
        if self.__is_it_my_turn(data):
            self.__think("Starting new turn for actor: {}".format(self.label))
        while True:
            if data["complete"]:
                return
            if not self.__is_it_my_turn(data):
                return data["public"]["turn"]["current_turn_actor_id"]
            old_turn_id = data["public"]["turn"]["id"]
            action = self.__get_action(data)
            if action is None:
                del self.prompt_card_map[data["public"]["turn"]["prompt"]["id"]]
                data = self.__get_game_info(fresh=True)
                continue
            data = self.__commit_action(action)
            if data["complete"]:
                return
            if data["public"]["turn"]["id"] != old_turn_id \
                    and data["public"]["turn"]["current_turn_actor_id"] != self.id:
                self.__think("My turn is complete!\n")
                return data["public"]["turn"]["current_turn_actor_id"]

    def __commit_action(self, action):
        return self.api_client.take_turn(
            game_id=self.game_id,
            actor_id=self.id,
            action=action)

    def __get_game_info(self, fresh=False):
        return self.api_client.load(self.game_id, self.id, fresh=fresh)

    def __is_it_my_turn(self, data):
        return not data["complete"] \
               and data["public"]["turn"] \
               and data["public"]["turn"]["current_turn_actor_id"] == self.id

    def __get_action(self, data):
        phase_type = data["public"]["phase_type"]
        # TODO: build definition APIs
        if phase_type == "Class Time":
            return self.__build_classtime_action(data)
        elif phase_type == "Dismissal":
            return self.__build_dismissal_action(data)
        return {}

    def _get_me(self, data):
        for actor in data["public"]["actors"]:
            if actor["id"] == self.id:
                return actor

    def __build_classtime_action(self, data):
        # cards in play:
        actor_data = self._get_me(data)
        cards_in_play = actor_data["in_play_effects"]["cards_in_play"]
        cards_in_play_names = ", ".join(["'{}'".format(c["template"]["name"]) for c in cards_in_play])
        self.__think("My cards in play: {}".format(cards_in_play_names))

        turn = data["public"]["turn"]
        card_id = self.__get_card_id(turn, actor_data["hand"])
        prompt = turn["prompt"]
        open_items = list(prompt["open"].items())
        for answer_key, open_prompt in open_items:
            prompt_options = open_prompt["options"]
            self.__enumerate_options(answer_key, prompt_options)
            if not prompt_options:
                self.__think("Skipping prompt", prompt["id"], "for card", card_id, "... no options")
                self.__set_card_prompt_map(prompt["id"], None)
                return
            selection = choice(prompt_options)
            prompt = self.answer(answer_key, prompt, selection)
        return {
            "card_id": card_id,
            "prompt": prompt,
            "type": "ActionCardAction"
        }

    def __enumerate_options(self, answer_key, prompt_options):
        self.__think("> Have a decision to make, '{}':".format(answer_key))
        print(prompt_options)
        for option in prompt_options:
            self.__think("   {}: {}".format(option["display"], option["id"]))

    def __get_card_id(self, turn, hand):
        card_id = self.prompt_card_map.get(turn["prompt"]["id"], False) or self.__choose_card(hand["action_cards"])
        self.__set_card_prompt_map(card_id, turn["prompt"]["id"])
        return card_id

    def __set_card_prompt_map(self, card_id, prompt_id):
        self.prompt_card_map[prompt_id] = card_id

    def __choose_card(self, hand):
        card_names = ", ".join(["'{}'".format(c["template"]["name"]) for c in hand])
        self.__think("My hand: {}".format(card_names))
        card_id = choice([ac["id"] for ac in hand])
        self.__think("I choose card:", self.__get_card_details(card_id, hand))
        return card_id

    @staticmethod
    def __think(*a):
        Logger.log(*a, level=LogLevel.Info, log_type=LogType.Ai)

    @staticmethod
    def __get_card_details(card_id, hand):
        for card in hand:
            if card["id"] == card_id:
                return "{}".format(card["template"]["name"])

    def __build_dismissal_action(self, data):
        turn = data["public"]["turn"]
        prompt = turn["prompt"]
        open_items = list(prompt["open"].items())
        for answer_key, open_prompt in open_items:
            prompt_options = open_prompt["options"]
            self.__enumerate_options(answer_key, prompt_options)
            if not prompt_options:
                self.__think("Skipping discipline prompt", prompt["pending"], "... no options")
                return
            selection = choice(prompt_options)
            prompt = self.answer(answer_key, prompt, selection)
        return {
            "prompt": prompt,
            "type": "DisciplineAction"
        }

    @staticmethod
    def answer(answer_key, prompt, selection):
        prompt["closed"][answer_key] = prompt["open"][answer_key]
        prompt["closed"][answer_key]["selected_option"] = selection
        del prompt["open"][answer_key]
        return prompt
