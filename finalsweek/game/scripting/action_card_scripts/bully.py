# +- ACTION CARD BOILERPLATE -------+
__locals = locals()
ActorApi = __locals.get('ActorApi')
StudentApi = __locals.get('StudentApi')
SeatApi = __locals.get('SeatApi')
PromptApi = __locals.get('PromptApi')
export = __locals.get('export')
# +- END ACTION CARD BOILERPLATE -------+


requestor = ActorApi.get_requestor()
eligible_students = StudentApi.get_adjacent_students(requestor.student)
selected_student = PromptApi.prompt_student_choice(eligible_students, "Target Student")
if selected_student.controlled:
    ActorApi.add_popularity(selected_student.actor, -5)
    ActorApi.add_torment(selected_student.actor, 1)
