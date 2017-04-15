requestor = StudentApi.get_requestor()
immediate_students = StudentApi.get_immediate_students(requestor)
empty_seats = SeatApi.get_empty_seats()

student_seat_actions = []
for student in immediate_students:
    selected_seat = PromptApi.prompt_seat_choice(empty_seats, "Target Seat for {}".format(student.id))
    student_seat_actions.append((student, selected_seat))

for student, seat in student_seat_actions:
    StudentApi.move_to_empty_seat(student, seat)

StudentApi.add_trouble(requestor, 1)
