from game.gameflow.actions.base import ActionBase
from game.systems.draw_manager import DrawManager


class RedrawAction(ActionBase):
    def __init__(self) -> None:
        super().__init__()
        self.draw_manager = DrawManager()

    def execute(self, actor_id, api):
        actor = api.actors.get(actor_id)
        self.draw_manager.refill_hand(actor, api)
