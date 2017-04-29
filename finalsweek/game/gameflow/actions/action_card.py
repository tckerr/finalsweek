from game.configuration.definitions import OperatorType, Tag, GameflowMessageType, LogType, LogLevel
from game.gameflow.actions.base import ActionBase
from game.operation.operations.modify_attribute import ModifyAttribute
from game.program_api.message_api import GameflowMessage
from game.scripting.action_card_script_runner import ActionCardScriptRunner
from logger import Logger


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
        exclusions = []
        if card.generates_mutation:
            mutation_template = card.template.mutation_template
            mutation = api.mutations.create_and_register(mutation_template, source_actor_id=actor_id, **result.exports)
            api.actors.transfer_card_to_in_play(actor_id, card.id, mutation.id)
            exclusions.append(mutation.id)
        else:
            message = "Expending action card {} for actor {}".format(self.card_id, actor_id)
            Logger.log(message, level=LogLevel.Info, log_type=LogType.GameLogic)
            api.actors.expend_action_card(actor_id, self.card_id)
        api.messenger.dispatch(GameflowMessage(GameflowMessageType.Action, actor_id=actor_id), exclude=exclusions)

    def _apply_trouble(self, api, actor_id, card):
        operation = ModifyAttribute(
            operator=OperatorType.Add,
            value=card.template.trouble_cost,
            targeted_actor_id=actor_id,
            tags=self._card_trouble_tags
        )
        api.actors.add_trouble(operation=operation)
        message = "Assigning {} trouble from action card {}".format(card.template.trouble_cost, self.card_id)
        Logger.log(message, level=LogLevel.Info, log_type=LogType.GameLogic)

    @property
    def _card_trouble_tags(self):
        return {Tag.Trouble, Tag.CardCost, Tag.ActionCardCost}
