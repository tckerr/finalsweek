# +- ACTION CARD BOILERPLATE -------+
__locals = locals()
ActorApi = __locals.get('ActorApi')
StudentApi = __locals.get('StudentApi')
SeatApi = __locals.get('SeatApi')
PromptApi = __locals.get('PromptApi')
export = __locals.get('export')
# +- END ACTION CARD BOILERPLATE -------+


all_seats = SeatApi.get_seats()
all_students = StudentApi.get_students()
selected_student = PromptApi.prompt_student_choice(all_students, "Target Student")

eligible_seats = list(filter(lambda s: s.id != selected_student.seat.id, all_seats))
selected_seat = PromptApi.prompt_seat_choice(eligible_seats, "Target Seat for {} ({})".format(selected_student.name, selected_student.id))

if selected_seat.empty:
    StudentApi.move_to_empty_seat(selected_student, selected_seat)
else:
    StudentApi.swap_seat(selected_student, selected_seat)
