requestor = StudentApi.get_requestor()
StudentApi.add_popularity(requestor, 3 * requestor.seat.row)
StudentApi.add_trouble(requestor, 3)
