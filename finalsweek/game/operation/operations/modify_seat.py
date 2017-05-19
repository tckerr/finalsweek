from game.definitions import OperationType
from game.operation.operations.operation import Operation


class ModifySeat(Operation):

    def __init__(self, destination_seat_id, targeted_student_id, tags) -> None:
        super().__init__(OperationType.ModifySeat, tags)
        self.destination_seat_id = destination_seat_id
        self.targeted_student_id = targeted_student_id
