from game.document.documents.phase import Phase
from game.document.seeding.phase_seed_factory import PhaseSeedFactory
from game.operation.mutation_adapter import MutationAdapter


class PhaseFactory(object):
    def __init__(self) -> None:
        super().__init__()
        self.mutation_adapter = MutationAdapter()
        self.phase_seed_factory = PhaseSeedFactory()

    def create(self, phase_type, stage, mutations):
        mutation_data = self.mutation_adapter.to_turn(mutations)
        phase_data = self.phase_seed_factory.create(phase_type, mutation_data)
        new_phase = Phase(phase_data, parent=stage)
        stage.phases.append(new_phase)
        return new_phase
