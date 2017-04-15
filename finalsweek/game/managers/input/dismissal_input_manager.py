from game.managers.input.input_manager_base import InputManagerBase

class DismissalInputManager(InputManagerBase):

    def __init__(self): pass

    def input(self, turn, action):
        actor = turn.actor
        seat = actor.seat
        self.__score_grades(seat, actor)
        actor.save()
        self._complete_turn(turn)


    def __score_grades(self, seat, actor):
        grades_score = self.__get_grades_score(seat)
        actor.grades += grades_score
        
        print("    + Incrementing grades by {} (row {})".format(grades_score, seat.row))

    def __get_grades_score(self, seat):
        return ( seat.row + 1 ) * 2
        