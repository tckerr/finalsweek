class DrawAction(object):
    def __init__(self, quantity, actor, card_type_id):
        self.quantity = quantity
        self.actor = actor
        self.card_type_id = card_type_id


class UseActionCardAction(object):
    def __init__(self, actor, card_id):
        self.actor = actor
        self.card_id = card_id