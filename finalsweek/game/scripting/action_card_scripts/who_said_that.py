requestor = ActorApi.get_requestor()
ActorApi.add_popularity(requestor, 3)
ActorApi.add_trouble(requestor, 2)
other_actors = ActorApi.get_all_but_requestor()
for actor in other_actors:
    ActorApi.set_trouble(actor, requestor.trouble)