requestor = ActorApi.get_requestor()
immediate_students = StudentApi.get_immediate_students(requestor.student)
empty_seats = SeatApi.get_empty_seats()

student_seat_actions = []
for student in immediate_students:
    selected_seat = PromptApi.prompt_seat_choice(empty_seats, "Target Seat for student {}".format(student.id))
    student_seat_actions.append((student, selected_seat))
    empty_seats = [s for s in empty_seats if s.id != selected_seat.id]

for student, seat in student_seat_actions:
    StudentApi.move_to_empty_seat(student, seat)

ActorApi.add_trouble(requestor, 1)
