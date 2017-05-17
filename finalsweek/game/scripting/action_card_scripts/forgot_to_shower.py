# +- ACTION CARD BOILERPLATE -------+
__locals = locals()
ActorApi = __locals.get('ActorApi')
StudentApi = __locals.get('StudentApi')
SeatApi = __locals.get('SeatApi')
PromptApi = __locals.get('PromptApi')
export = __locals.get('export')
# +- END ACTION CARD BOILERPLATE -------+


requestor = ActorApi.get_requestor()
immediate_students = StudentApi.get_immediate_students(requestor.student)
empty_seats = SeatApi.get_empty_seats()

student_seat_actions = []
for student in immediate_students:
    selected_seat = PromptApi.prompt_seat_choice(empty_seats, "Target Seat for Student {} ({})".format(student.name, student.id))
    student_seat_actions.append((student, selected_seat))
    empty_seats.remove(selected_seat)

for student, seat in student_seat_actions:
    StudentApi.move_to_empty_seat(student, seat)
