requestor = StudentApi.get_requestor()
if requestor.torment > 0:
    StudentApi.add_torment(requestor, -1)
    StudentApi.add_popularity(requestor, 5)
StudentApi.add_trouble(requestor, 1)