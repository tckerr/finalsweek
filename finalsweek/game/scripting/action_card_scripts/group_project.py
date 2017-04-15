all_actors = ActorApi.get_actors()
for actor in all_actors:
    ActorApi.add_grades(actor, 8)
requestor = ActorApi.get_requestor()
ActorApi.add_popularity(requestor, 4)