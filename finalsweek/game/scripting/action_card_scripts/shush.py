requestor = ActorApi.get_requestor()
ActorApi.add_grades(requestor, 8)
adjacent_students_count = len(StudentApi.get_adjacent_students(requestor.student))
ActorApi.add_popularity(requestor, -adjacent_students_count)