# +- DISCIPLINE CARD BOILERPLATE -------+
__locals = locals()
ActorApi = __locals.get('ActorApi')
StudentApi = __locals.get('StudentApi')
SeatApi = __locals.get('SeatApi')
export = __locals.get('export')
# +- END DISCIPLINE CARD BOILERPLATE -------+

actor = ActorApi.get_requestor()
trouble = min(actor.trouble, 5)
if trouble > 0:
    ActorApi.add_popularity(actor, -2 * trouble)
