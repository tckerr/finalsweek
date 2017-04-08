class ActorSummary(object):
    def __init__(self, actor, perspective):
        self.id = actor.id
        self.action_hand_count = len(actor.action_hand.cards.all())
        if perspective.actor_id == actor.id:
            self.__init_private_fields(actor)

    def __init_private_fields(self, actor):
        self.action_hand = actor.action_hand