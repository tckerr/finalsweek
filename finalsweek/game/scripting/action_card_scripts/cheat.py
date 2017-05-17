# +- ACTION CARD BOILERPLATE -------+
__locals = locals()
ActorApi = __locals.get('ActorApi')
StudentApi = __locals.get('StudentApi')
SeatApi = __locals.get('SeatApi')
PromptApi = __locals.get('PromptApi')
export = __locals.get('export')
# +- END ACTION CARD BOILERPLATE -------+


trouble_amount = PromptApi.prompt_number_choice(list(range(1, 6)), "Trouble Amount")
requestor = ActorApi.get_requestor()
ActorApi.add_trouble(requestor, trouble_amount)
ActorApi.add_grades(requestor, 2 * trouble_amount)
