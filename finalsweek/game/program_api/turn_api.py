from datetime import datetime

from game.document.document_factories.turn_factory import TurnFactory
from game.gameflow.flowstate.providers import CurrentTurnProvider
from game.scripting.api.program_child_api import ProgramChildApi


class TurnApi(ProgramChildApi):
    def __init__(self, program_api) -> None:
        super().__init__(program_api)
        self.turn_factory = TurnFactory()
        self.current_turn_provider = CurrentTurnProvider()

    def get_or_create_current_turn(self, fresh=False):
        return self.current_turn_provider.get_or_create_turn(self.program_api, fresh)

    def get_current_turn(self):
        return self.current_turn_provider.get_current_turn(self.program_api)

    def create_turn(self, phase_id, actor_id):
        for stage in self.data.gameflow.stages:
            for phase in stage.phases:
                if phase.id == phase_id:
                    return self._create_turn(actor_id, phase)
        raise Exception("Phase {} not found.".format(phase_id))

    def _create_turn(self, actor_id, phase):
        return self.turn_factory.create(actor_id, phase, [])

    def list_turns(self):
        for stage in self.data.gameflow.stages:
            for phase in stage.phases:
                for turn in phase.turns:
                    yield turn

    def complete_turn(self, turn_id):
        for turn in self.list_turns():
            if turn.id == turn_id:
                return self._complete(turn)
        raise Exception("Turn not found: {}".format(turn_id))

    @staticmethod
    def _complete(turn):
        turn.completed = datetime.utcnow()

    def refresh_current_turn(self, turn_id):
        turn = self.get_or_create_current_turn()
        assert turn.id == turn_id
        turn.refresh()
