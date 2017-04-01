from sim.messaging.message_types import MessageTypes
from sim.entity.components import TurnComponent
from sim.exceptions import GameFlowViolation
import random

class GameMocker(object):

    def mock(self, game_manager):
        messages = (
            #( MessageTypes.GradesModification, {"value": 15, "target_entity_id": 1} ),
            #( MessageTypes.ReportGrades, ),
            ( MessageTypes.DebugValues, ),
        )

        for message in messages:
            game_manager.message_dispatcher.dispatch(*message)

    def performance_test(self, game_manager):
        start = datetime.now()        
        mock_message = ( MessageTypes.DebugValues, {"value": "hello world"} )
        game_manager.message_dispatcher.dispatch(*mock_message)
        end = datetime.now()
        elapsed = end - start
        print("Time to dispatch 1 message to {} entities:".format(str(game_manager.game.total_actors)), elapsed.total_seconds())
        

    def turn_test(self, game_manager, rounds=10):

        for round_number in range(1, rounds+1):
            print ("   [Starting round {}]".format(str(round_number)))

            if game_manager.turn_manager.needs_turn_assignment():
                game_manager.turn_manager.initialize_next_turn()

            turns = TurnComponent.objects.filter(entity__game=game_manager.game)
            print (turns.count())
            assert turns.count() == 1
            entity = TurnComponent.objects.filter(entity__game=game_manager.game).first().entity
            print ("      It is entity({})'s turn".format(str(entity.id)))
            while game_manager.turn_manager.entity_has_turn(entity):
                cost = random.randint(1,2)
                try:
                    print("      Attempting action of cost ({})".format(str(cost)))
                    game_manager.turn_manager.expend_action(entity, cost)
                    
                except GameFlowViolation as e:
                    print("         Invalid Request!", e)
            print("      Turn complete!")