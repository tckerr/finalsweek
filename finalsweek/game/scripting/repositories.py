from game.models import Actor, Seat, Student

class ScriptContextRepository(object):

    def __init__(self, requestor):
        self.requestor_id = requestor.id
        self.game_id = requestor.game_id
    
    def actors(self):
        if not hasattr(self, "_actors_cache"):
            qs = Actor.objects.filter(game_id=self.game_id).prefetch_related("student__seat")
            self._actors_cache = list(qs)
        return self._actors_cache

    def students(self):
        if not hasattr(self, "_students_cache"):
            qs = Student.objects.filter(seat__game_id=self.game_id).prefetch_related("seat")
            self._students_cache = list(qs)
        return self._students_cache

    def requestor(self):
        actors = self.actors()
        return next(filter(lambda s: s.id == self.requestor_id, actors))

    def seats(self):
        if not hasattr(self, "_seats_cache"):
            qs = Seat.objects.filter(game_id=self.game_id).prefetch_related("student__actor")
            self._seats_cache = list(qs)
        return self._seats_cache
