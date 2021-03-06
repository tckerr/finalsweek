from game.gameflow.action_eligibility_resolver import ActionEligibilityResolver
from game.gameflow.actions.factories import AutomatedActionFactory
from trace.logger import Logger
from trace.definitions import LogLevel, LogType


class ActionExecutor(object):
    def __init__(self):
        super(ActionExecutor, self).__init__()
        self.action_eligibility_resolver = ActionEligibilityResolver()
        self.automated_action_factory = AutomatedActionFactory()

    def execute(self, turn, action, api):
        self.action_eligibility_resolver.validate(action, turn)
        phase_definition = api.phases.get_phase_definition(turn.phase.phase_type)
        self._execute(api, action, turn, phase_definition)
        return self._next_actor_turn(api)  # this may be same turn if prompt=true

    def _next_actor_turn(self, api):
        while True:
            turn = api.turns.get_or_create_current_turn()
            if not turn:
                return

            phase_definition = api.phases.get_phase_definition(turn.phase.phase_type)
            if phase_definition.automatic:
                action = self.automated_action_factory.create(phase_definition)
                # TODO: ASSUMPTION: no prompts from automated turns?
                self._execute(api, action, turn, phase_definition)
            else:
                return turn

    def _execute(self, api, action, turn, phase_definition):
        self._log_turn_details(api, action, turn.actor_id, phase_definition.phase_type)

        prompt_data = action.execute(turn.actor_id, api)
        if prompt_data:
            # Todo: move these operations to a PromptApi
            turn.prompt.open = prompt_data["open"]
            turn.prompt.closed = prompt_data["closed"]
        else:
            api.turns.complete_turn(turn.id)

    @staticmethod
    def _log_turn_details(api, action, actor_id, phase_type):
        actor = api.actors.get(actor_id)
        action_class_name = type(action).__name__
        template = "Executing phase: '{phase}' with action '{action}' for actor '{actor}': {summary}"
        message = template.format(
            phase=phase_type,
            action=action_class_name,
            actor=actor.label,
            summary=actor.summary)
        Logger.log(message, level=LogLevel.Info, log_type=LogType.GameLogic)
