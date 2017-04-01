class Rules(object):
    def __init__(self, total_actors):
        self.total_actors = total_actors
        self.auto_create_ai = True

class SaveState(object):

    def __init__(self, id=None):
        self.id = id
        self.component_entity_map = None
        self.rules = Rules()
