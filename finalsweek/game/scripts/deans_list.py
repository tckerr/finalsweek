requestor = StudentApi.get_requestor()
other_students = StudentApi.get_all_but_requestor()
if requestor.grades > max([s.grades for s in other_students]):
    StudentApi.add_popularity(requestor, 9)