# +- ACTION CARD BOILERPLATE -------+
__locals = locals()
ActorApi = __locals.get('ActorApi')
StudentApi = __locals.get('StudentApi')
SeatApi = __locals.get('SeatApi')
PromptApi = __locals.get('PromptApi')
export = __locals.get('export')
# +- END ACTION CARD BOILERPLATE -------+


requestor = ActorApi.get_requestor()
empty_seats = SeatApi.get_empty_seats()
requestor_row = requestor.student.seat.row
empty_seats_ahead_of_requestor = list(filter(lambda s: s.row < requestor_row, empty_seats))

selected_seat = PromptApi.prompt_seat_choice(empty_seats_ahead_of_requestor, "Target Seat")

row_diff = requestor_row - selected_seat.row
StudentApi.move_to_empty_seat(requestor.student, selected_seat)
ActorApi.add_grades(requestor, 2 * row_diff)
