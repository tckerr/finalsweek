requestor = StudentApi.get_requestor()
StudentApi.add_popularity(requestor, 3)
StudentApi.add_trouble(requestor, 2)
other_students = StudentApi.get_all_but_requestor()
for student in other_students:
    StudentApi.set_trouble(student, requestor.trouble)