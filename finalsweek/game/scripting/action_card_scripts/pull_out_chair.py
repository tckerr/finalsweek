# +- ACTION CARD BOILERPLATE -------+
__locals = locals()
ActorApi = __locals.get('ActorApi')
StudentApi = __locals.get('StudentApi')
SeatApi = __locals.get('SeatApi')
PromptApi = __locals.get('PromptApi')
export = __locals.get('export')
# +- END ACTION CARD BOILERPLATE -------+


requestor = ActorApi.get_requestor()
eligible_actors = ActorApi.get_adjacent_actors(requestor)
selected_actor = PromptApi.prompt_actor_choice(eligible_actors, "Target Actor")
ActorApi.subtract_popularity(selected_actor, 6)
