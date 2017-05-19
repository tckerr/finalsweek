# +- ACTION CARD BOILERPLATE -------+
__locals = locals()
ActorApi = __locals.get('ActorApi')
StudentApi = __locals.get('StudentApi')
SeatApi = __locals.get('SeatApi')
PromptApi = __locals.get('PromptApi')
export = __locals.get('export')
# +- END ACTION CARD BOILERPLATE -------+


requestor = ActorApi.get_requestor()
ActorApi.add_grades(requestor, 8)
adjacent_students_count = len(StudentApi.get_adjacent_students(requestor.student))
ActorApi.subtract_popularity(requestor, adjacent_students_count)
