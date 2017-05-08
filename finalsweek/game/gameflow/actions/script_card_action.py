from abc import ABCMeta, abstractmethod

from game.gameflow.actions.base import ActionBase
from game.systems.card_mutation_generator import CardMutationGenerator


class ScriptCardAction(ActionBase):
    __metaclass__ = ABCMeta

    def __init__(self, data) -> None:
        super().__init__(data)
        self.card_mutation_generator = CardMutationGenerator()

    def execute(self, actor_id, api):
        super().execute(actor_id, api)
        card = self._get_card(actor_id, api)
        script = card.template.script
        result = self._run_script(actor_id, api, script)
        if result.complete:
            self._resolve_completion(actor_id, api, card, result)
        return result.prompt

    @abstractmethod
    def _get_card(self, actor_id, api):
        raise NotImplemented("Method '_get_card' must be implemented in all derived classes.")

    @abstractmethod
    def _run_script(self, actor_id, api, script):
        raise NotImplemented("Method '_run_script' must be implemented in all derived classes.")

    @abstractmethod
    def _resolve_completion(self, actor_id, api, card, result):
        raise NotImplemented("Method '_resolve_completion' must be implemented in all derived classes.")