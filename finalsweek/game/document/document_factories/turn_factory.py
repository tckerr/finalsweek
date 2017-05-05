from game.document.documents.turn import Turn
from game.document.seeding.turn_seed_factory import TurnSeedFactory
from game.operation.mutation_adapter import MutationAdapter


class TurnFactory(object):
    def __init__(self) -> None:
        super().__init__()
        self.turn_seed_factory = TurnSeedFactory()
        self.mutation_adapter = MutationAdapter()

    def create(self, actor_id, phase, mutations):
        mutation_data = self.mutation_adapter.to_turn(mutations)
        turn_data = self.turn_seed_factory.create(actor_id, mutation_data)
        turn = Turn(turn_data, parent=phase)
        phase.turns.append(turn)
        return turn


