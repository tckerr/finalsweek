seats = SeatApi.get_seats()
students = StudentApi.get_students()
selected_student = PromptApi.prompt_student_choice(students, "Target Student")

eligible_seats = list(filter(lambda s: s.id != selected_student.seat.id, seats))
selected_seat = PromptApi.prompt_seat_choice(eligible_seats, "Target Seat for {}".format(selected_student.id))

if selected_seat.empty:
    StudentApi.move_to_empty_seat(selected_student, selected_seat)
else:
    StudentApi.swap_seat(selected_student, selected_seat)