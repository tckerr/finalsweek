from game.summaries.game_summary import GameSummary

class GameSummaryBuilder(object):
    def build(self, game, current_turn, perspective):
        complete = current_turn is None
        if not complete:
            stage = current_turn.phase.stage.stage_type_id
            phase = current_turn.phase.phase_type_id
            current_turn_actor_id = current_turn.actor.id
        else:
            stage = "Scoring"
            phase = "Score"
            current_turn_actor_id = None
            
        actors = game.actors.prefetch_related("action_hand__cards").all()
        return GameSummary(actors, stage, phase, complete, current_turn_actor_id, perspective)
 