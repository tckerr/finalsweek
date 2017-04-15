trouble_amount = PromptApi.prompt_number_choice(list(range(1, 6)), "Trouble Amount")
requestor = StudentApi.get_requestor()
StudentApi.add_trouble(requestor, trouble_amount)
StudentApi.add_grades(requestor, 2 * trouble_amount)