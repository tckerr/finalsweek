# +- DISCIPLINE CARD BOILERPLATE -------+
__locals = locals()
ActorApi = __locals.get('ActorApi')
StudentApi = __locals.get('StudentApi')
SeatApi = __locals.get('SeatApi')
export = __locals.get('export')
# +- END DISCIPLINE CARD BOILERPLATE -------+

actor = ActorApi.get_requestor()
trouble = actor.trouble
if trouble == 0:
    ActorApi.add_grades(actor, 4)
elif trouble > 3:
    ActorApi.subtract_grades(actor, 2)
