requestor = StudentApi.get_requestor()
eligible_students = StudentApi.get_adjacent_students(requestor)
selected_student = PromptApi.prompt_student_choice(eligible_students, "Target Student")
StudentApi.add_torment(selected_student, -1)
StudentApi.add_trouble(requestor, -2)