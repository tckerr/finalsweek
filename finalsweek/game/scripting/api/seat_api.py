from game.scripting.api.sandbox_api import SandboxApi

class SeatApi(SandboxApi):

    def get_seats(self):
        return self.repo.seats()

    def get_filled_seats(self):
        seats = self.get_seats()
        return list(filter(lambda s: not s.empty, seats))

    def get_empty_seats(self):
        seats = self.get_seats()
        return list(filter(lambda s: s.empty, seats))

    def get_adjacent_seats(self, seat):
        seats = self.get_seats()
        results = []
        for s in seats:
            col_diff = abs(s.column - seat.column)
            row_diff = abs(s.row - seat.row)
            if col_diff <= 1 and row_diff <= 1 and (row_diff + col_diff) != 0:
                results.append(s)
        return results
