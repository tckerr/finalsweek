from game.definitions import OperatorType, Tag
from game.operation.operations.modify_attribute import ModifyAttribute
from trace.definitions import LogLevel, LogType
from trace.logger import Logger


class ActionCardTroubleApplier(object):
    def apply(self, api, actor, card):
        operation = ModifyAttribute(
            operator=OperatorType.Add,
            value=card.template.trouble_cost,
            targeted_actor_id=actor.id,
            tags=self._card_trouble_tags
        )
        api.actors.add_trouble(operation=operation)
        self._log_trouble_application(actor, card)

    @staticmethod
    def _log_trouble_application(actor, card):
        template = "Assigning {} {} trouble from action card {}"
        message = template.format(actor.label, card.template.trouble_cost, card.id)
        Logger.log(message, level=LogLevel.Info, log_type=LogType.GameLogic)

    @property
    def _card_trouble_tags(self):
        return {Tag.Trouble, Tag.CardCost, Tag.ActionCardCost}
