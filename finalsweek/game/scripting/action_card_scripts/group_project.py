# +- ACTION CARD BOILERPLATE -------+
__locals = locals()
ActorApi = __locals.get('ActorApi')
StudentApi = __locals.get('StudentApi')
SeatApi = __locals.get('SeatApi')
PromptApi = __locals.get('PromptApi')
export = __locals.get('export')
# +- END ACTION CARD BOILERPLATE -------+


all_actors = ActorApi.get_actors()
for actor in all_actors:
    ActorApi.add_grades(actor, 8)
requestor = ActorApi.get_requestor()
ActorApi.add_popularity(requestor, 4)
