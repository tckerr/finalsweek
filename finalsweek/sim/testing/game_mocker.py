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
        start = datetime.utcnow()        
        mock_message = ( MessageTypes.DebugValues, {"value": "hello world"} )
        game_manager.message_dispatcher.dispatch(*mock_message)
        end = datetime.utcnow()
        elapsed = end - start
        print("Time to dispatch 1 message to {} entities:".format(str(game_manager.game.total_actors)), elapsed.total_seconds())
        

    def turn_test(self, game_manager):
        while True:
            # this will be provided somewhere else
            new_entity_id, round_number = self.__get_current_turn_entity_id(game_manager.game.id)
            print ("   [Round {}]".format(str(round_number)))
            print ("      It is entity({})'s turn".format(str(new_entity_id)))
            cost = random.randint(1,2)
            try:
                print("      Attempting action of cost ({})".format(str(cost)))
                game_manager.expend_action(new_entity_id, cost)
                
            except GameFlowViolation as e:
                print("         Invalid Request!", e)
            

    # hack to get something that will be public knowledge later
    def __get_current_turn_entity_id(self, game_id):
        component = TurnComponent.objects.filter(entity__game_id=game_id, expended__isnull=True).first()
        return component.entity.id, component.round_number