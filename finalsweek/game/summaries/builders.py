from game.summaries.game_summary import GameSummary

class GameSummaryBuilder(object):
    def build(self, game, current_turn):
        actors = game.actors.all()
        return GameSummary(actors, current_turn)