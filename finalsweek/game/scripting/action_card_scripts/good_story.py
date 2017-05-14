# +- ACTION CARD BOILERPLATE -------+
__locals = locals()
ActorApi = __locals.get('ActorApi')
StudentApi = __locals.get('StudentApi')
SeatApi = __locals.get('SeatApi')
PromptApi = __locals.get('PromptApi')
export = __locals.get('export')
# +- END ACTION CARD BOILERPLATE -------+


requestor = ActorApi.get_requestor()
eligible_students = StudentApi.get_all_but_requestor()
adjacent_seats = SeatApi.get_adjacent_seats(requestor.student.seat)
empty_seats = [s for s in adjacent_seats if s.empty]

selected_student1 = PromptApi.prompt_student_choice(eligible_students, "Target Student 1")
selected_seat1 = PromptApi.prompt_seat_choice(empty_seats, "Target Student 1 Seat")

empty_seats = [s for s in empty_seats if s is not selected_seat1]
selected_student2 = PromptApi.prompt_student_choice(eligible_students, "Target Student 2")
selected_seat2 = PromptApi.prompt_seat_choice(empty_seats, "Target Student 2 Seat")

StudentApi.move_to_empty_seat(selected_student1, selected_seat1)
StudentApi.move_to_empty_seat(selected_student2, selected_seat2)
