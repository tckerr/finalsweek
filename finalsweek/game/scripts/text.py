requestor = StudentApi.get_requestor()
eligible_students = StudentApi.get_all_but_requestor()
selected_student = PromptApi.prompt_student_choice(eligible_students, "Target Student")
if selected_student.popularity > requestor.popularity:
    StudentApi.add_popularity(requestor, 10)
else:
    StudentApi.add_popularity(requestor, 5)

if selected_student.seat.row == 0:
    StudentApi.add_trouble(selected_student, 1)
    
StudentApi.add_trouble(requestor, 2)