from game.scripting.trusted_script_runner import ActionCardScriptRunner
from game.systems.draw_manager import HandRefiller


class ActionBase(object):
    def execute(self, actor_id, api):
        pass


class ChooseSeatAction(ActionBase):
    pass
    # TODO: implement choices here (the seats are already chosen at this point)
    # this may have to be out of the game because actors only exist on seats ATM


class RedrawToFullAction(ActionBase):
    def __init__(self) -> None:
        super().__init__()
        self.hand_refiller = HandRefiller()

    def execute(self, actor_id, api):
        actor = api.actors.get_actor(actor_id)
        self.hand_refiller.refill_hand(actor, api)


class ActionCardAction(ActionBase):
    def __init__(self, card_id, prompt) -> None:
        super().__init__()
        self.prompt = prompt
        self.card_id = card_id
        self.trusted_script_runner = ActionCardScriptRunner()

    def execute(self, actor_id, api):
        super().execute(actor_id, api)
        card = api.actors.get_action_card_by_actor(actor_id, self.card_id)
        script = card.template.script
        prompt = self.trusted_script_runner.run(actor_id, api, script, self.prompt)
        if not prompt:
            api.actors.expend_action_card(actor_id, self.card_id)
        return prompt
