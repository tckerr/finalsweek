requestor = ActorApi.get_requestor()
requestor_row = requestor.student.seat.row
ActorApi.add_popularity(requestor, 3 * requestor_row)
ActorApi.add_trouble(requestor, 3)
