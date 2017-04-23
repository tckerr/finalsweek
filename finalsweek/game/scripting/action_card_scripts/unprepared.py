eligible_actors = ActorApi.get_all_but_requestor()
selected_actor = PromptApi.prompt_actor_choice(eligible_actors, "Target Actor")
ActorApi.add_grades(selected_actor, -4)
