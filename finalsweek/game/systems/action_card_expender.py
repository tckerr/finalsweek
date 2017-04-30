from game.configuration.definitions import LogLevel, LogType
from logger import Logger


class ActionCardExpender(object):
    def expend(self, actor, api, card_id):
        self._log_card_expense(actor, card_id)
        api.actors.expend_action_card(actor.id, card_id)

    @staticmethod
    def _log_card_expense(actor, card_id):
        message = "Expending action card {} for actor {}".format(card_id, actor.label)
        Logger.log(message, level=LogLevel.Info, log_type=LogType.GameLogic)
