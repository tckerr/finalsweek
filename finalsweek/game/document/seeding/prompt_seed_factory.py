from game.document.documents.prompt import Prompt
from util.random import random_id


class PromptSeedFactory(object):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def create():
        return Prompt({
            "id":     random_id(),
            "open":   {},
            "closed": {},
            "context_id": None
        })
