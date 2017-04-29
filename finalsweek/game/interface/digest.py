class GameDigest(object):
    def __init__(self) -> None:
        self.complete = False


class CardTemplateDigest(GameDigest):
    def __init__(self, card_template):
        super().__init__()
        self.id = card_template.id
        self.card_type = card_template.card_type
        self.name = card_template.name
        self.trouble_cost = card_template.trouble_cost


class CardInfoDigest(GameDigest):
    def __init__(self, card):
        super().__init__()
        self.id = card.id
        self.template = CardTemplateDigest(card.template)


class ActorDigest(GameDigest):
    def __init__(self, actor):
        super().__init__()
        self.id = actor.id
        self.label = actor.label
        self.name = actor.name


class GameInfoDigest(GameDigest):
    def __init__(self, game_id, api):
        super().__init__()
        self.game_id = game_id
        self.actors = [ActorDigest(actor) for actor in api.actors.list()]


class HandDigest(GameDigest):
    def __init__(self, requesting_actor_id, api):
        super().__init__()
        requesting_actor = api.actors.get(requesting_actor_id)
        action_card_hand = requesting_actor.action_card_hand
        self.action_cards = [CardInfoDigest(card) for card in action_card_hand.cards]


class TurnDigest(GameDigest):
    def __init__(self, requesting_actor_id, turn, api):
        super().__init__()
        self.current_turn_actor_id = turn.actor_id
        self.phase_type = turn.phase.phase_type
        self.stage_type = turn.phase.stage.stage_type
        self.hand = HandDigest(requesting_actor_id, api)
        self.prompt = turn.prompt
        self.id = turn.id


class InPlayEffectDigest(GameDigest):
    def __init__(self, requesting_actor_id, api):
        super().__init__()
        requesting_actor = api.actors.get(requesting_actor_id)
        cards_in_play = requesting_actor.cards_in_play
        self.cards_in_play = [CardInfoDigest(ipe.card) for ipe in cards_in_play]


class GeneralDigest(GameDigest):
    def __init__(self, game_info_digest, turn_digest=None, in_play_effect_digest=None):
        super().__init__()
        self.game_info = game_info_digest
        self.turn = turn_digest
        self.in_play_effects = in_play_effect_digest


class GameOverDigest(object):
    def __init__(self, game_info_digest) -> None:
        super().__init__()
        self.game_info = game_info_digest
        self.complete = True


class DigestProvider(object):
    @staticmethod
    def game_info_digest(game_id, api):
        game_info_digest = GameInfoDigest(game_id, api)
        return GeneralDigest(game_info_digest)

    @staticmethod
    def general_digest(game_id, api, turn, requesting_actor_id):
        game_info_digest = GameInfoDigest(game_id, api)
        if not turn:
            return GameOverDigest(game_info_digest)
        turn_digest = TurnDigest(requesting_actor_id, turn, api)
        in_play_effect_digest = InPlayEffectDigest(requesting_actor_id, api)
        return GeneralDigest(game_info_digest, turn_digest=turn_digest, in_play_effect_digest=in_play_effect_digest)
