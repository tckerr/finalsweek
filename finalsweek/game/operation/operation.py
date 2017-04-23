class OperationType(object):
    # mod types
    DefineEligibility = "DefineEligibility"  # target is being selected for something
    ModifyAttribute = "ModifyAttribute"  # target has already been selected and is getting some change
    ExtractInfo = "ExtractInfo"  # target is being selected for non-public info


class Operation(object):
    def __init__(self, operation_type, metadata) -> None:
        super().__init__()
        self.operation_type = operation_type
        self.metadata = metadata


class DefineEligibility(Operation):
    def __init__(self, metadata) -> None:
        operation_type = OperationType.DefineEligibility
        super().__init__(operation_type, metadata)


class ModifyAttribute(Operation):
    def __init__(self, metadata) -> None:
        operation_type = OperationType.ModifyAttribute
        super().__init__(operation_type, metadata)
