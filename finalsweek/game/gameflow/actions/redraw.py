from game.gameflow.actions.base import ActionBase
from game.systems.draw_manager import HandRefiller


class RedrawAction(ActionBase):
    def __init__(self) -> None:
        super().__init__()
        self.hand_refiller = HandRefiller()

    def execute(self, actor_id, api):
        actor = api.actors.get_actor(actor_id)
        self.hand_refiller.refill_hand(actor, api)
