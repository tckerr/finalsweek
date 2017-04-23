requestor = ActorApi.get_requestor()
ActorApi.add_popularity(requestor, 3 * requestor.trouble)
ActorApi.add_trouble(requestor, 2)
