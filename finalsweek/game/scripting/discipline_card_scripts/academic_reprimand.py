# +- DISCIPLINE CARD BOILERPLATE -------+
__locals = locals()
ActorApi = __locals.get('ActorApi')
StudentApi = __locals.get('StudentApi')
SeatApi = __locals.get('SeatApi')
export = __locals.get('export')
# +- END DISCIPLINE CARD BOILERPLATE -------+

penalties = {
    1: 1,
    2: 2,
    3: 4,
    4: 5
}
actor = ActorApi.get_requestor()
trouble = min(actor.trouble, 4)
if trouble > 0:
    ActorApi.subtract_grades(actor, penalties[trouble])
