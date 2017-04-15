eligible_students = StudentApi.get_students()
selected_student = PromptApi.prompt_student_choice(eligible_students, "Target Student")
StudentApi.add_trouble(selected_student, 2)