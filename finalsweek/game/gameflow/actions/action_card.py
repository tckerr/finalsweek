from game.gameflow.actions.base import ActionBase
from game.scripting.action_card_script_runner import ActionCardScriptRunner


class ActionCardScriptRunnerFactory(object):
    def create(self, actor_id, turn_prompt):
        return ActionCardScriptRunner(actor_id, turn_prompt)

class ActionCardAction(ActionBase):
    def __init__(self, card_id, prompt) -> None:
        super().__init__()
        self.prompt = prompt
        self.card_id = card_id
        self.trusted_script_runner_factory = ActionCardScriptRunnerFactory()

    def execute(self, actor_id, api):
        super().execute(actor_id, api)
        card = api.actors.get_action_card_by_actor(actor_id, self.card_id)
        script = card.template.script
        runner = self.trusted_script_runner_factory.create(actor_id, self.prompt)
        result = runner.run(api, script)
        if result.complete:
            self.resolve_card_completion(actor_id, api, card, result)
        return result.prompt

    def resolve_card_completion(self, actor_id, api, card, result):
        if card.generates_mutation:
            mutation_template = card.template.mutation_template
            mutation = api.mutations.create_and_register(mutation_template, **result.exports)
            api.actors.transfer_card_to_in_play(actor_id, card.id, mutation.id)
        else:
            api.actors.expend_action_card(actor_id, self.card_id)
