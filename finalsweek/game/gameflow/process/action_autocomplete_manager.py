from game.gameflow.process.action_executor import ActionExecutor
from game.gameflow.process.action_factories import AutomatedActionFactory


class ActionAutocompleteManager(object):
    def __init__(self):
        self.action_executor = ActionExecutor()
        self.automated_action_factory = AutomatedActionFactory()

    def action_and_automate(self, action, api, turn):
        while True:
            self.action_executor.execute(turn, action, api)  # make prompts stateful?
            turn = api.turns.get_current_turn()
            if not turn:
                return None
            phase_definition = api.phases.get_phase_definition(turn.phase.phase_type)
            if not phase_definition.automatic:
                break
            action = self.automated_action_factory.create(phase_definition)
        return turn
