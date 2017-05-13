class Digest(object):
    @property
    def data(self):
        return {}


class CardTemplateDigest(Digest):
    def __init__(self, card_template):
        super().__init__()
        self.id = card_template.id
        self.card_type = card_template.card_type
        self.name = card_template.name
        self.trouble_cost = card_template.trouble_cost
        self.description = card_template.description

    @property
    def data(self):
        return {
            "id":           self.id,
            "card_type":    self.card_type,
            "name":         self.name,
            "description":  self.description,
            "trouble_cost": self.trouble_cost
        }


class CardInfoDigest(Digest):
    def __init__(self, card):
        super().__init__()
        self.id = card.id
        self.template = CardTemplateDigest(card.template)

    @property
    def data(self):
        return {
            "id":       self.id,
            "template": self.template.data
        }


class ActorDigest(Digest):
    def __init__(self, actor, api):
        super().__init__()
        self.id = actor.id
        self.label = actor.label
        self.name = actor.name
        self.in_play_effects = InPlayEffectDigest(actor.id, api)
        self.hand = HandDigest(actor.id, api)  # TODO: make hand private
        self.stats = {
            "grades":     actor.grades,
            "popularity": actor.popularity,
            "trouble":    actor.trouble,
            "torment":    actor.torment
        }
        self.seat = {
            "row": actor.seat.row,
            "column": actor.seat.column
        }

    @property
    def data(self):
        return {
            "id":              self.id,
            "label":           self.label,
            "name":            self.name,
            "hand":            self.hand.data,
            "in_play_effects": self.in_play_effects.data,
            "stats":           self.stats,
            "seat":            self.seat,
        }


class PublicDigest(Digest):
    def __init__(self, game_id, api, turn):
        super().__init__()
        self.game_id = game_id
        self.actors = [ActorDigest(actor, api) for actor in api.actors.list()]
        self.phase_type = turn.phase.phase_type if turn else "Complete"
        self.stage_type = turn.phase.stage.stage_type if turn else "Complete"
        self.turn = TurnDigest(turn, api) if turn else None

    @property
    def data(self):
        return {
            "game_id":    str(self.game_id),
            "turn":       self.turn.data if self.turn else {},
            "actors":     [a.data for a in self.actors],
            "phase_type": self.phase_type,
            "stage_type": self.stage_type,
        }


class PrivateDigest(Digest):
    def __init__(self, turn):
        super().__init__()
        self.turn = turn

    @property
    def data(self):
        return {
            "turn": self.turn.data,
        }


class HandDigest(Digest):
    def __init__(self, requesting_actor_id, api):
        super().__init__()
        requesting_actor = api.actors.get(requesting_actor_id)
        action_card_hand = requesting_actor.action_card_hand
        self.action_cards = [CardInfoDigest(card) for card in action_card_hand.cards]

    @property
    def data(self):
        return {
            "action_cards": [a.data for a in self.action_cards]
        }


class TurnDigest(Digest):
    def __init__(self, turn, api):
        super().__init__()
        self.current_turn_actor_id = turn.actor_id
        self.prompt = turn.prompt
        self.id = turn.id

    @property
    def data(self):
        return {
            "current_turn_actor_id": self.current_turn_actor_id,
            "prompt":                self.prompt.data,
            "id":                    self.id
        }


class InPlayEffectDigest(Digest):
    def __init__(self, requesting_actor_id, api):
        super().__init__()
        requesting_actor = api.actors.get(requesting_actor_id)
        cards_in_play = requesting_actor.cards_in_play
        self.cards_in_play = [CardInfoDigest(ipe.card) for ipe in cards_in_play]

    @property
    def data(self):
        return {
            "cards_in_play": [a.data for a in self.cards_in_play]
        }


class ResponseDigest(Digest):
    def __init__(self, public, complete=False):
        super().__init__()
        self.public = public
        self.complete = complete

    @property
    def data(self):
        return {
            "public":   self.public.data,
            "complete": self.complete
        }


class DigestProvider(object):
    @staticmethod
    def general_digest(game_id, api, turn):
        public_digest = PublicDigest(game_id, api, turn)
        return ResponseDigest(public_digest, complete=turn is None)
