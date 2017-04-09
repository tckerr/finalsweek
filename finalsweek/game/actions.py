class DrawAction(object):
    def __init__(self, quantity, actor_id, card_type_id):
        self.quantity = quantity
        self.actor_id = actor_id
        self.card_type_id = card_type_id

class UseActionCardAction(object):
    def __init__(self, actor_id, decisions):
        self.actor_id = actor_id
        self.card_name = decisions["card_name"]
        #example
        self.decisions = decisions