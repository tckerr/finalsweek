# +- ACTION CARD BOILERPLATE -------+
__locals = locals()
ActorApi = __locals.get('ActorApi')
StudentApi = __locals.get('StudentApi')
SeatApi = __locals.get('SeatApi')
PromptApi = __locals.get('PromptApi')
export = __locals.get('export')
# +- END ACTION CARD BOILERPLATE -------+


requestor = ActorApi.get_requestor()
eligible_actors = ActorApi.get_all_but_requestor()
selected_actor = PromptApi.prompt_actor_choice(eligible_actors, "Target Actor")
if selected_actor.popularity > requestor.popularity:
    ActorApi.add_popularity(requestor, 10)
else:
    ActorApi.add_popularity(requestor, 5)

if selected_actor.student.seat.row == 0:
    ActorApi.add_trouble(selected_actor, 1)
