requestor = StudentApi.get_requestor()
empty_seats = SeatApi.get_empty_seats()
empty_seats_ahead_of_requestor = list(filter(lambda s: s.row < requestor.seat.row, empty_seats))

selected_seat = PromptApi.prompt_seat_choice(empty_seats_ahead_of_requestor, "Target Seat")

row_diff = requestor.seat.row - selected_seat.row
StudentApi.move_to_empty_seat(requestor, selected_seat)
StudentApi.add_grades(requestor, 2 * row_diff)
