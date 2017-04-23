trouble_amount = PromptApi.prompt_number_choice(list(range(1, 6)), "Trouble Amount")
requestor = ActorApi.get_requestor()
ActorApi.add_trouble(requestor, trouble_amount)
ActorApi.add_grades(requestor, 2 * trouble_amount)
