all_students = StudentApi.get_students()
for student in all_students:
    StudentApi.add_grades(student, 8)
requestor = StudentApi.get_requestor()
StudentApi.add_popularity(requestor, 4)