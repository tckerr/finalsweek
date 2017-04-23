requestor = ActorApi.get_requestor()
other_students = ActorApi.get_all_but_requestor()
if requestor.grades > max([s.grades for s in other_students]):
    ActorApi.add_popularity(requestor, 9)
