from game.document.documents.prompt import Prompt
from game.gameflow.actions.script_card_action import ScriptCardAction
from game.scripting.played_card_script_runner import ActionCardScriptRunner
from game.systems.action_card_expender import ActionCardExpender
from game.systems.action_card_trouble_applier import ActionCardTroubleApplier


class ActionCardAction(ScriptCardAction):
    def __init__(self, data) -> None:
        super().__init__(data)
        self.prompt = Prompt(data["prompt"]) # TODO: make not just data but actual prompt
        self.card_id = data["card_id"]
        self.action_card_trouble_applier = ActionCardTroubleApplier()
        self.action_card_expender = ActionCardExpender()

    def _get_card(self, actor_id, api):
        return api.actors.get_action_card_by_actor(actor_id, self.card_id)

    def _run_script(self, actor_id, api, script):
        runner = ActionCardScriptRunner(actor_id, self.prompt)
        result = runner.run(api, script)
        return result

    def _resolve_completion(self, actor_id, api, card, result):
        actor = api.actors.get(actor_id)
        self.action_card_trouble_applier.apply(api, actor, card)
        if card.generates_mutation:
            self.card_mutation_generator.generate(actor_id, api, card, result)
        else:
            self.action_card_expender.expend(actor, api, self.card_id)