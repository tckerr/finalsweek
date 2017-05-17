from game.document.documents.document_base import DocumentBase, IdDict
from game.document.documents.mutation import Mutation


class MutationQueue(DocumentBase):
    _field_definitions = {
        "mutations":    Mutation
    }

    def __init__(self, base_data, parent=None):
        super().__init__(base_data, parent)


class MutationQueueIdDict(IdDict):
    cls = MutationQueue
