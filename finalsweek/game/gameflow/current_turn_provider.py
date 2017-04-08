from game.gameflow.generators import StageGenerator, PhaseGenerator, TurnGenerator, Reset
from game.gameflow.action_automater import ActionAutomater

class CurrentTurnProvider(object):
    def __init__(self, take_turn_proxy):
        self.stage_generator = StageGenerator()
        self.phase_generator = PhaseGenerator()
        self.turn_generator = TurnGenerator()
        self.action_automater = ActionAutomater(take_turn_proxy)

    def get(self, game):
        loop = 0
        while True:
            loop += 1
            try:
                stage = self.stage_generator.get_or_generate(game)
                if stage is None:
                    return
                phase = self.phase_generator.get_or_generate(stage)
                next_turn = self.turn_generator.get_or_generate(phase)
                return self.action_automater.automate_if_needed(next_turn)
            except Reset as e:
                if loop > 10:
                    raise Exception("Loop > 10")
                continue