from game.summaries.actor_summary import ActorSummary

class GameSummary(object):
    def __init__(self, actors, stage, phase, complete, current_turn_actor_id, perspective):
        self.stage = stage
        self.phase = phase
        self.complete = complete
        self.actors = [ActorSummary(actor, perspective) for actor in actors if actor.id != perspective.actor_id]
        self.current_turn_actor_id = current_turn_actor_id

        # find me and set me
        me_candidates = list(filter(lambda a: a.id == perspective.actor_id, actors))
        if me_candidates:
            self.me = ActorSummary(me_candidates[0], perspective)
