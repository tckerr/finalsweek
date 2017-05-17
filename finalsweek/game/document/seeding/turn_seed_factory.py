from game.document.seeding.prompt_seed_factory import PromptSeedFactory
from util.random import random_id


class TurnSeedFactory(object):
    def __init__(self) -> None:
        super().__init__()
        self.prompt_seed_factory = PromptSeedFactory()

    def create(self, actor_id, mutations):
        return {
            "id":        random_id(),
            "actor_id":  actor_id,
            "log":       [],
            "completed": None,
            "prompt":    self.prompt_seed_factory.create(),
            "mutations": mutations
        }