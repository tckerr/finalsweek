from game.configuration.definitions import LogType, LogLevel
from game.gameflow.actions.factories import AutomatedActionFactory
from logger import log, Logger


class ActionExecutor(object):
    def __init__(self):
        super(ActionExecutor, self).__init__()
        self.automated_action_factory = AutomatedActionFactory()

    def execute(self, turn, action, api):
        phase_definition = api.phases.get_phase_definition(turn.phase.phase_type)
        self._execute(api, action, turn, phase_definition)
        return self._next_actor_turn(api)  # this may be same turn if prompt=true

    def _next_actor_turn(self, api):
        while True:
            turn = api.turns.get_current_turn()
            if not turn:
                return

            phase_definition = api.phases.get_phase_definition(turn.phase.phase_type)
            if phase_definition.automatic:
                action = self.automated_action_factory.create(phase_definition)
                # ASSUMPTION: no prompts from automated turns
                self._execute(api, action, turn, phase_definition)
            else:
                return turn

    def _execute(self, api, action, turn, phase_definition):
        self._log_turn_details(api, action, turn.actor_id, phase_definition.phase_type)
        # Todo: save prompt if it exists
        prompt_data = action.execute(turn.actor_id, api)
        if prompt_data:
            turn.prompt.open = prompt_data["open"]
            turn.prompt.closed = prompt_data["closed"]
        else:
            api.turns.complete_turn(turn.id)

    @staticmethod
    def _log_turn_details(api, action, actor_id, phase_type):
        actor = api.actors.get_actor(actor_id)
        action_class_name = type(action).__name__
        message = "Executing phase: '{phase}' with action '{action}' for actor '{actor}'".format(
            phase=phase_type,
            action=action_class_name,
            actor=actor.label)
        Logger.log(message, level=LogLevel.Info, log_type=LogType.GameLogic)
