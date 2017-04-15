eligible_students = StudentApi.get_all_but_requestor()
selected_student = PromptApi.prompt_student_choice(eligible_students, "Target Student")
StudentApi.add_grades(selected_student, -4)