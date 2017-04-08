from django.utils import timezone

class InputManagerBase(object):
    def _complete_turn(self, turn):
        turn.completed=timezone.now()
        turn.save()

    def input(self, turn, action):
        self._complete_turn(turn)