from game.models import Turn 

class StagePrefetchRepository(object):

    def get(self, game):
        return game.stages.prefetch_related("phases__turns__actor")

class PendingTurnRepository(object):

    def get(self, game):
        pending = Turn \
            .objects.filter(phase__stage__game=game,completed__isnull=True)\
            .prefetch_related("phase__stage__game__actors")\
            .all()
        return list(pending)