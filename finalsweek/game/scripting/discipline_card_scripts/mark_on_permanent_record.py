# +- DISCIPLINE CARD BOILERPLATE -------+
__locals = locals()
ActorApi = __locals.get('ActorApi')
StudentApi = __locals.get('StudentApi')
SeatApi = __locals.get('SeatApi')
export = __locals.get('export')
# +- END DISCIPLINE CARD BOILERPLATE -------+

for actor in ActorApi.get_actors():
    trouble = actor.trouble
    ActorApi.add_grades(actor, -trouble)
    ActorApi.add_popularity(actor, -trouble)
