from game.document.seeding.student_seed_factory import StudentSeedFactory
from util.util import guid


class SeatSeedFactory(object):
    def __init__(self) -> None:
        super().__init__()
        self.student_seed_factory = StudentSeedFactory()

    def create(self, settings, student_infos, player_count):
        seats = []
        total = settings["total_students"]
        for row in range(0, settings["seat_rows"]):
            for column in range(0, settings["seat_columns"]):
                seat = {
                    "id":      guid(),
                    "row":     row,
                    "column":  column,
                    "student": None
                }
                if total > 0:
                    seat["student"] = self.student_seed_factory.create(student_infos, player_count > 0)
                    total -= 1
                    player_count -= 1
                seats.append(seat)
        return seats
