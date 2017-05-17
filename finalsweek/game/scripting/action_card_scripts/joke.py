# +- ACTION CARD BOILERPLATE -------+
__locals = locals()
ActorApi = __locals.get('ActorApi')
StudentApi = __locals.get('StudentApi')
SeatApi = __locals.get('SeatApi')
PromptApi = __locals.get('PromptApi')
export = __locals.get('export')
# +- END ACTION CARD BOILERPLATE -------+

requestor = ActorApi.get_requestor()
adjacent_students = StudentApi.get_adjacent_students(requestor.student)
adjacent_students_count = len(adjacent_students)
ActorApi.add_popularity(requestor, adjacent_students_count)
