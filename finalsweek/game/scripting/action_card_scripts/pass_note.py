requestor = ActorApi.get_requestor()
seats = SeatApi.get_filled_seats()
r_seat = requestor.student.seat

eligible_seats = []
for s in seats:
    if s.id != r_seat.id and (s.row == r_seat.row or s.column == r_seat.column) and s.student is not None:
        eligible_seats.append(s)
eligible_students = [s.student for s in eligible_seats]

selected_student = PromptApi.prompt_student_choice(eligible_students, "Target Student")

s_seat = selected_student.seat
field = "column" if s_seat.column != r_seat.column else "row"

r_seat_dim = getattr(r_seat, field)
s_seat_dim = getattr(s_seat, field)
max_dim = max(r_seat_dim, s_seat_dim)
min_dim = min(r_seat_dim, s_seat_dim)
in_between = lambda s: getattr(s, field) <= max_dim and getattr(s, field) >= min_dim

eligible_seats = filter(lambda s: s.id != r_seat.id, seats)
matching_seats = filter(in_between, eligible_seats)
value = 3 * len(list(matching_seats))

ActorApi.add_popularity(requestor, value)
