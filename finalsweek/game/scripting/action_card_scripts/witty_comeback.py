requestor = ActorApi.get_requestor()
if requestor.torment > 0:
    ActorApi.add_torment(requestor, -1)
    ActorApi.add_popularity(requestor, 5)
ActorApi.add_trouble(requestor, 1)
