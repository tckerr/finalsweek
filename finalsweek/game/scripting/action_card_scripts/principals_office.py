eligible_actors = ActorApi.get_actors()
selected_actor = PromptApi.prompt_actor_choice(eligible_actors, "Target Actor")
ActorApi.add_trouble(selected_actor, 2)