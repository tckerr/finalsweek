from game.factories import GameFactory, ActorFactory
from game.ensurers import GameCreationEnsurer
from game.managers.input.input_manager_resolver import InputManagerResolver
from game.summaries.builders import GameSummaryBuilder
from game.gameflow.current_turn_provider import CurrentTurnProvider
from game.gameflow.action_automater import ActionAutomater
from game.actions import UseActionCardAction
from game.options import CardTargetOperationSetChoiceBuilder

class Perspective(object):
    def __init__(self, actor_id):
        self.actor_id = actor_id

class TurnSummary(object): pass

class ActionCardOptionBuilder(object):
    def __init__(self):
        self.card_target_operation_set_choice_builder = CardTargetOperationSetChoiceBuilder()

    def build(self, current_turn, card, decisions):
        card_decisions = decisions.get(card.id, {})
        card_target_operation_sets = card.card_target_operation_sets.order_by('execution_order')
        return { cto.id: self.card_target_operation_set_choice_builder.build(current_turn, cto, card_decisions) for cto in card_target_operation_sets }

class TurnOptionBuilder(object):
    # TODO, we can early exit if this isnt chosen yet
    def __init__(self):
        self.action_card_option_builder = ActionCardOptionBuilder()

    def build(self, current_turn, decisions):
        phase = current_turn.phase.phase_type_id
        if phase == "Classtime":
            action_cards = list(current_turn.actor.action_hand.cards.all())
            seen = []
            hand = []
            for card in action_cards:
                if card.id not in seen:
                    hand.append(card)
                    seen.append(card.id)
            return { card.id: self.action_card_option_builder.build(current_turn, card, decisions) for card in hand }



class GameRouter(object):

    def __init__(self):
        self.game_creation_ensurer = GameCreationEnsurer()
        self.game_factory = GameFactory()
        self.actor_factory = ActorFactory()
        self.input_manager_resolver = InputManagerResolver()        
        self.game_summary_builder = GameSummaryBuilder()
        self.current_turn_provider = CurrentTurnProvider()
        self.action_automater = ActionAutomater(self.take_turn)
        self.turn_option_builder = TurnOptionBuilder()

    def create(self, player_count):
        self.game_creation_ensurer.ensure()
        game = self.game_factory.create(player_count)
        return self.__build_summary(game)    
    
    def __load(self, actor_id):
        game_id = self.actor_factory.load(actor_id).game_id
        return self.game_factory.load(game_id)  
    
    def load(self, actor_id,):
        game = self.__load(actor_id)       
        return self.__build_summary(game, actor_id)    

    def take_turn(self, actor_id, action=None):
        actor = self.actor_factory.load(actor_id)
        turns = actor.turns.filter(completed__isnull=True)
        if not turns:
            raise Exception("Not your turn!")
        if turns.count() > 1:
            raise Exception("More than 1 turn!")
        turn = turns.first()
        self.input_manager_resolver.resolve(turn, action) # true if it did anything        
        return self.load(actor_id)

    def take_turn_desc(self, actor_id, decisions):
        actor = self.actor_factory.load(actor_id)
        turns = actor.turns.filter(completed__isnull=True)
        if not turns:
            raise Exception("Not your turn!")
        if turns.count() > 1:
            raise Exception("More than 1 turn!")
        turn = turns.first()
        action = UseActionCardAction(actor_id, decisions)
        self.input_manager_resolver.resolve(turn, action) # true if it did anything        
        return self.load(actor_id)

    def get_turn_options(self, actor_id, decisions):
        game = self.__load(actor_id)
        current_turn = self.__automate_until_user_action_needed(game)
        if current_turn.actor.id != actor_id:
            return None
        return self.turn_option_builder.build(current_turn, decisions)

    def __build_summary(self, game, actor_id=None):
        current_turn = self.__automate_until_user_action_needed(game)
        return self.game_summary_builder.build(game, current_turn, perspective=Perspective(actor_id))

    def __automate_until_user_action_needed(self, game):
        next_turn = self.current_turn_provider.get(game)
        if self.action_automater.automate_if_needed(next_turn):
            return self.__automate_until_user_action_needed(game)
        return next_turn

