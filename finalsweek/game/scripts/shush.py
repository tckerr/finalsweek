requestor = StudentApi.get_requestor()
StudentApi.add_grades(requestor, 8)
adjacent_students_count = len(StudentApi.get_adjacent_students(requestor))
StudentApi.add_popularity(requestor, -adjacent_students_count)