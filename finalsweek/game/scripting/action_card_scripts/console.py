requestor = ActorApi.get_requestor()
eligible_students = StudentApi.get_adjacent_students(requestor.student)
selected_student = PromptApi.prompt_student_choice(eligible_students, "Target Student")
if selected_student.controlled:
    ActorApi.add_torment(selected_student.actor, -1)
ActorApi.add_trouble(requestor, -2)
