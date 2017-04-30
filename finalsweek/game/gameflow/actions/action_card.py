from game.configuration.definitions import GameflowMessageType
from game.gameflow.actions.base import ActionBase
from game.program_api.message_api import GameflowMessage
from game.scripting.played_card_script_runner import PlayedCardScriptRunner
from game.systems.action_card_expender import ActionCardExpender
from game.systems.action_card_mutation_generator import ActionCardMutationGenerator
from game.systems.action_card_trouble_applier import ActionCardTroubleApplier


class ActionCardAction(ActionBase):
    def __init__(self, card_id, prompt) -> None:
        super().__init__()
        self.prompt = prompt
        self.card_id = card_id
        self.action_card_trouble_applier = ActionCardTroubleApplier()
        self.action_card_mutation_generator = ActionCardMutationGenerator()
        self.action_card_expender = ActionCardExpender()

    def execute(self, actor_id, api):
        super().execute(actor_id, api)
        card = api.actors.get_action_card_by_actor(actor_id, self.card_id)
        result = self._run_script(actor_id, api, card)
        if result.complete:
            self._resolve_card_completion(actor_id, api, card, result)
        return result.prompt

    def _run_script(self, actor_id, api, card):
        script = card.template.script
        runner = PlayedCardScriptRunner(actor_id, self.prompt)
        result = runner.run(api, script)
        return result

    def _resolve_card_completion(self, actor_id, api, card, result):
        actor = api.actors.get(actor_id)
        self.action_card_trouble_applier.apply(api, actor, card)
        exclusions = []
        if card.generates_mutation:
            exclusion = self.action_card_mutation_generator.generate(actor_id, api, card, result)
            exclusions.append(exclusion)
        else:
            self.action_card_expender.expend(actor, api, self.card_id)
        self._dispatch_action_message(actor_id, api, exclusions)

    @staticmethod
    def _dispatch_action_message(actor_id, api, exclusions):
        api.messenger.dispatch(GameflowMessage(GameflowMessageType.Action, actor_id=actor_id), exclude=exclusions)
