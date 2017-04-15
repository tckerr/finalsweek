requestor = StudentApi.get_requestor()
StudentApi.add_popularity(requestor, 3 * requestor.trouble)
StudentApi.add_trouble(requestor, 2)