class DrawAction(object):
    def __init__(self, quantity, actor_id, card_type_id):
        self.quantity = quantity
        self.actor_id = actor_id
        self.card_type_id = card_type_id

class UseActionCardAction(object):
    def __init__(self, actor_id, pc_id, decisions):
        self.actor_id = actor_id
        self.pc_id = pc_id
        #example
        self.decisions = decisions