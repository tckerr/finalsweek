from game.configuration.definitions import OperatorType, Tag
from game.gameflow.actions.base import ActionBase
from game.operation.operations.modify_attribute import ModifyAttribute
from game.scripting.action_card_script_runner import ActionCardScriptRunner


class ActionCardScriptRunnerFactory(object):
    @staticmethod
    def create(actor_id, turn_prompt):
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
        self._apply_trouble(api, actor_id,  card)
        if card.generates_mutation:
            mutation_template = card.template.mutation_template
            mutation = api.mutations.create_and_register(mutation_template, source_actor_id=actor_id, **result.exports)
            api.actors.transfer_card_to_in_play(actor_id, card.id, mutation.id)
        else:
            api.actors.expend_action_card(actor_id, self.card_id)

    def _apply_trouble(self, api, actor_id, card):
        operation = ModifyAttribute(
            operator=OperatorType.Add,
            value=card.template.trouble_cost,
            targeted_actor_id=actor_id,
            tags=self._card_trouble_tags
        )
        api.actors.add_trouble(operation=operation)

    @property
    def _card_trouble_tags(self):
        return {Tag.Trouble, Tag.CardCost, Tag.ActionCardCost}
