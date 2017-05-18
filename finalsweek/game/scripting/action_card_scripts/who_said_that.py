# +- ACTION CARD BOILERPLATE -------+
__locals = locals()
ActorApi = __locals.get('ActorApi')
StudentApi = __locals.get('StudentApi')
SeatApi = __locals.get('SeatApi')
PromptApi = __locals.get('PromptApi')
export = __locals.get('export')
# +- END ACTION CARD BOILERPLATE -------+


requestor = ActorApi.get_requestor()
ActorApi.add_popularity(requestor, 3)
ActorApi.add_trouble(requestor, 2)
other_actors = ActorApi.get_all_but_requestor()
for actor in other_actors:
    ActorApi.set_trouble(actor, requestor.trouble)
