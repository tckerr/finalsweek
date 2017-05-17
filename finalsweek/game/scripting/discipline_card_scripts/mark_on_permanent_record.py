# +- DISCIPLINE CARD BOILERPLATE -------+
__locals = locals()
ActorApi = __locals.get('ActorApi')
StudentApi = __locals.get('StudentApi')
SeatApi = __locals.get('SeatApi')
export = __locals.get('export')
# +- END DISCIPLINE CARD BOILERPLATE -------+

actor = ActorApi.get_requestor()
trouble = actor.trouble
ActorApi.add_grades(actor, -trouble)
ActorApi.add_popularity(actor, -trouble)
