class ActionAutomater(object):
    def __init__(self, take_turn_proxy):
        self.take_turn_proxy = take_turn_proxy

    def automate_if_needed(self, turn):
        if self.__requires_automation(turn):
            self.__log(turn)
            response = self.take_turn_proxy(turn.actor_id, None)
            return True
        return False

    def __requires_automation(self, turn):
        return turn and turn.phase.phase_type.is_automatic

    def __log(self, turn):
        print("> System is automating: Stage: {stage}, Phase: {phase}, Actor {actor_id}'s turn".format(
            stage=str(turn.phase.stage.stage_type_id), 
            phase=str(turn.phase.phase_type_id), 
            actor_id=str(turn.actor.id)))
