from game.models import Actor, Seat

class ScriptContextRepository(object):

    def __init__(self, requestor):
        self.requestor_id = requestor.id
        self.game_id = requestor.game_id
    
    def students(self):
        if not hasattr(self, "_students_cache"):
            kwargs = {"game_id": self.game_id}
            self._students_cache = self.__model_list(Actor, kwargs)
        return self._students_cache

    def requestor(self):
        students = self.students()
        return next(filter(lambda s: s.id == self.requestor_id, students))

    def seats(self):
        if not hasattr(self, "_seats_cache"):
            kwargs = {"game_id": self.game_id}
            self._seats_cache = self.__model_list(Seat, kwargs)
        return self._seats_cache

    def __model_list(self, model_class, kwargs):
        return list(model_class.objects.filter(**kwargs))