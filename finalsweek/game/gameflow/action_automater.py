from game.resolvers import AutomaticActionResolver

class ActionAutomater(object):
    def __init__(self, take_turn_proxy):
        self.automatic_action_resolver = AutomaticActionResolver()
        self.take_turn_proxy = take_turn_proxy

    def automate_if_needed(self, turn):
        if self.__requires_automation(turn):
            print("> System is automating: Stage: {}, Phase: {}, Actor {}'s turn".format(str(turn.phase.stage.stage_type_id), str(turn.phase.phase_type_id), str(turn.actor.id)))
            auto_action = self.automatic_action_resolver.resolve(turn)
            response = self.take_turn_proxy(turn.actor_id, auto_action)
            return True
        return False

    def __requires_automation(self, turn):
        return turn and turn.phase.phase_type.is_automatic