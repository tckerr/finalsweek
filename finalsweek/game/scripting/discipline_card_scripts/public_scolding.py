# +- DISCIPLINE CARD BOILERPLATE -------+
__locals = locals()
ActorApi = __locals.get('ActorApi')
StudentApi = __locals.get('StudentApi')
SeatApi = __locals.get('SeatApi')
export = __locals.get('export')
# +- END DISCIPLINE CARD BOILERPLATE -------+

for actor in ActorApi.get_actors():
    trouble = min(actor.trouble, 5)
    if trouble < 2:
        continue
    ActorApi.add_torment(actor, 1)
    if trouble == 4:
        ActorApi.add_popularity(actor, -3)
    elif trouble > 4:
        ActorApi.add_popularity(actor, -6)
