from game.definitions import OperatorType, OperationType
from game.operation.operations.operation import Operation


class Draw(Operation):
    valid_operators = (OperatorType.Add,)

    def __init__(self, operator, value, targeted_actor_id, tags) -> None:
        super().__init__(OperationType.Draw, tags)
        if operator not in self.valid_operators:
            raise Exception("Operator '{}' is invalid for operation type '{}'".format(operator, "ModifyAttribute"))
        self.operator = operator
        self.value = value
        self.targeted_actor_id = targeted_actor_id
