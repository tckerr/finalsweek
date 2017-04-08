class DrawAction(object):
    def __init__(self, quantity, actor_id, card_type_id):
        self.quantity = quantity
        self.actor_id = actor_id
        self.card_type_id = card_type_id


class UseActionCardAction(object):
    def __init__(self, actor_id, card_id):
        self.actor_id = actor_id
        self.card_id = card_id