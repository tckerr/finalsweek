# +- DISCIPLINE CARD BOILERPLATE -------+
__locals = locals()
ActorApi = __locals.get('ActorApi')
StudentApi = __locals.get('StudentApi')
SeatApi = __locals.get('SeatApi')
export = __locals.get('export')
# +- END DISCIPLINE CARD BOILERPLATE -------+

penalties = {
    1: -1,
    2: -2,
    3: -4,
    4: -5
}

for actor in ActorApi.get_actors():
    trouble = min(actor.trouble, 4)
    if trouble == 0:
        continue
    ActorApi.add_grades(actor, penalties[trouble])
