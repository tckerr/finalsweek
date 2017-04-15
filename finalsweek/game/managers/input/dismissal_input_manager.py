from game.managers.input.input_manager_base import InputManagerBase
from game.models import PileCard
from game.managers.draw_manager import HandRefiller

class DismissalInputManager(InputManagerBase):

    def __init__(self):
        self.__hand_refiller = HandRefiller()

    def input(self, turn, action):
        actor = turn.actor
        seat = actor.seat
        self.__refill_hand(actor)
        self.__score_grades(seat, actor)
        self.__resolve_discipline()
        actor.save()
        self._complete_turn(turn)


    def __refill_hand(self, actor):
        self.__hand_refiller.refill_hand(actor)

    def __score_grades(self, seat, actor):
        grades_score = self.__get_grades_score(seat)
        actor.grades += grades_score        
        print("    + Incrementing grades by {} (row {})".format(grades_score, seat.row))

    def __get_grades_score(self, seat):
        return ( seat.row + 1 ) * 2

    def __resolve_discipline(self):
        print ("    + Resolving discipline... (placeholder)")
        
