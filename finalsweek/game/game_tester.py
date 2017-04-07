from game.factories import GameFactory, ActorFactory
from game.providers import StageProvider, PhaseProvider, TurnProvider, Reset
from game.ensurers import TypeEnsurer, StudentInfoEnsurer, CardTypeEnsurer, CardEnsurer
from game.managers import InputManager
from game.resolvers import AutomaticActionResolver

class GameManager(object):

    def __init__(self):
        self.type_ensurer = TypeEnsurer()
        self.student_info_ensurer = StudentInfoEnsurer()
        self.card_type_ensurer = CardTypeEnsurer()
        self.card_ensurer = CardEnsurer()
        self.game_factory = GameFactory()
        self.actor_factory = ActorFactory()
        self.stage_provider = StageProvider()
        self.phase_provider = PhaseProvider()
        self.turn_provider = TurnProvider()
        self.input_manager = InputManager()
        self.automatic_action_resolver = AutomaticActionResolver()

    def create(self):
        self.student_info_ensurer.ensure()
        self.type_ensurer.ensure() 
        self.card_type_ensurer.ensure() 
        self.card_ensurer.ensure() 
        game = self.game_factory.create(4)
        return self.load(game.id)
    
    def load(self, game_id, count=0):
        try:                       
            game = self.game_factory.load(game_id) 
            stage = self.stage_provider.provide(game)
            if stage is None:
                return
            phase = self.phase_provider.provide(stage)
            next_turn = self.turn_provider.provide(phase)
            return self.__automate_if_needed(next_turn)
        except Reset as e:
            good = False if count > 20 else True           
        if good:
            return self.load(game_id, count+1)
        else:
            raise Exception("At least 20 resets() called...")

    def __automate_if_needed(self, next_turn):
        if self.__requires_automation(next_turn):
            print("> System is automating: Stage: {}, Phase: {}, Actor {}'s turn".format(str(next_turn.phase.stage.stage_type_id), str(next_turn.phase.phase_type_id), str(next_turn.actor.id)))
            auto_action = self.automatic_action_resolver.resolve(next_turn)
            return self.take_turn(next_turn.actor_id, auto_action)
        return next_turn

    def __requires_automation(self, next_turn):
        return not next_turn or next_turn.phase.phase_type.is_automatic

    def take_turn(self, actor_id, action=None):

        actor = self.actor_factory.load(actor_id)
        turns = actor.turns.filter(completed__isnull=True)
        if not turns:
            raise Exception("Not your turn!")
        if turns.count() > 1:
            raise Exception("More than 1 turn!")
        turn = turns.first()
        self.input_manager.input(turn, action) # true if it did anything        
        return self.load(actor.game_id)




