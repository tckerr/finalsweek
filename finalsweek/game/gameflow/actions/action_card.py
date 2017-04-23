from game.gameflow.actions.base import ActionBase
from game.scripting.action_card_script_runner import ActionCardScriptRunner


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
