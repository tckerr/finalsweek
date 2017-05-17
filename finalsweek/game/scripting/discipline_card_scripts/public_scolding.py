# +- DISCIPLINE CARD BOILERPLATE -------+
__locals = locals()
ActorApi = __locals.get('ActorApi')
StudentApi = __locals.get('StudentApi')
SeatApi = __locals.get('SeatApi')
export = __locals.get('export')
# +- END DISCIPLINE CARD BOILERPLATE -------+

actor = ActorApi.get_requestor()
trouble = min(actor.trouble, 5)
if trouble >= 2:
    ActorApi.add_torment(actor, 1)
    if trouble == 4:
        ActorApi.add_popularity(actor, -3)
    elif trouble > 4:
        ActorApi.add_popularity(actor, -6)
