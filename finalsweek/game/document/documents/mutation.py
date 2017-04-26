from game.document.documents.document_base import DocumentBase
from game.document.documents.operation_metadata import OperationMetadata


class Mutation(DocumentBase):
    _field_definitions = {
        "id":       str,
        "criteria": OperationMetadata,
        "priority": int
    }

    def __init__(self, base_data, parent=None):
        self.criteria = None
        super().__init__(base_data, parent)

    def mutate_on_match(self, operation):
        if not self.criteria.matches(operation.metadata):
            print("No match, returning operation...")
            return operation
        print("Matched, but for now just returning operation...")
        return operation
