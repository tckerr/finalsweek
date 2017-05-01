# +- DISCIPLINE CARD BOILERPLATE -------+
__locals = locals()
ActorApi = __locals.get('ActorApi')
StudentApi = __locals.get('StudentApi')
SeatApi = __locals.get('SeatApi')
PromptApi = __locals.get('PromptApi')
export = __locals.get('export')
# +- END DISCIPLINE CARD BOILERPLATE -------+

actor = ActorApi.get_requestor()

if actor.trouble == 1:
    ActorApi.add_popularity(actor, 4)
elif actor.trouble in (2, 3):
    ActorApi.add_popularity(actor, 2)

export("targeted_actor_id", actor.id)