from game.scripting.api.base import ProgramChildApi


class SeatApi(ProgramChildApi):
    def list_seats(self):
        return self.data.seats

    def get_seat(self, seat_id):
        for seat in self.list_seats():
            if seat.id == seat_id:
                return seat
        raise Exception("Seat not found: {}".format(seat_id))