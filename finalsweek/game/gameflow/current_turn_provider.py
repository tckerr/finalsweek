from game.gameflow.generators import StageGenerator, PhaseGenerator, TurnGenerator, Reset

class CurrentTurnProvider(object):
    def __init__(self):
        self.stage_generator = StageGenerator()
        self.phase_generator = PhaseGenerator()
        self.turn_generator = TurnGenerator()

    def get(self, game):
        loop = 0
        while True:
            loop += 1
            try:
                stage = self.stage_generator.get_or_generate(game)
                if stage is None:
                    return
                phase = self.phase_generator.get_or_generate(stage)
                return self.turn_generator.get_or_generate(phase)
            except Reset as e:
                if loop > 10:
                    raise Exception("Loop > 10")
                continue