from game.document.documents.phase import Phase
from game.document.seeding.phase_seed_factory import PhaseSeedFactory
from game.operation.mutation_adapter import MutationAdapter
from trace.logger import Logger
from trace.definitions import LogLevel, LogType


class PhaseFactory(object):
    def __init__(self) -> None:
        super().__init__()
        self.mutation_adapter = MutationAdapter()
        self.phase_seed_factory = PhaseSeedFactory()

    def create(self, phase_type, stage, mutations):
        self._log_mutations(mutations)
        mutation_data = self.mutation_adapter.to_phase(mutations)
        phase_data = self.phase_seed_factory.create(phase_type, mutation_data)
        new_phase = Phase(phase_data, parent=stage)
        stage.phases.append(new_phase)
        return new_phase

    @staticmethod
    def _log_mutations(mutations):
        if mutations:
            log_message = "Adding queued mutations (count: {}) to new phase.".format(len(mutations))
        else:
            log_message = "No mutations to add to new phase."
        Logger.log(log_message, level=LogLevel.Debug, log_type=LogType.GameLogic)
