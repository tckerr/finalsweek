from game.document.documents.operation_metadata import OperationMetadata


class OperationType(object):
    # mod types
    DefineEligibility = "DefineEligibility"  # target is being selected for something
    ModifyAttribute = "ModifyAttribute"  # target has already been selected and is getting some change
    ExtractInfo = "ExtractInfo"  # target is being selected for non-public info


class OperatorType(object):
    Add = "Add"
    Set = "Set"
    Get = "Get"


class Operation(object):
    def __init__(self, operation_type, metadata: OperationMetadata) -> None:
        assert issubclass(metadata.__class__, OperationMetadata)
        super().__init__()
        self.operation_type = operation_type
        self.metadata = metadata


class DefineEligibility(Operation):
    def __init__(self, metadata) -> None:
        operation_type = OperationType.DefineEligibility
        super().__init__(operation_type, metadata)


class ModifyAttribute(Operation):
    valid_operators = (OperatorType.Add, OperatorType.Set)

    def __init__(self, operator, value, actor_id, metadata) -> None:
        super().__init__(OperationType.ModifyAttribute, metadata)
        if operator not in self.valid_operators:
            raise Exception("Operator '{}' is invalid for operation type '{}'".format(operator, "ModifyAttribute"))
        self.operator = operator
        self.value = value
        self.actor_id = actor_id
