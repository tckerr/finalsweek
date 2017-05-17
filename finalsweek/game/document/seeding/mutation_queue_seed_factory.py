from game.document.documents.mutation_queue import MutationQueue


class MutationQueueSeedFactory(object):
    @staticmethod
    def create():
        return {
            "mutations": [],
        }


class MutationQueueFactory(object):
    def __init__(self):
        self.mutation_queue_seed_factory = MutationQueueSeedFactory()

    def create(self):
        data = self.mutation_queue_seed_factory.create()
        return MutationQueue(data)
