from game.configuration.definitions import Tag, OperatorType
from game.operation.operations.modify_attribute import ModifyAttribute
from game.scripting.api.sandbox_api import SandboxApi


class ActorApi(SandboxApi):
    def __init__(self, *args, **kwargs):
        super(ActorApi, self).__init__(*args, **kwargs)

    def get_actors(self):
        return self._sort_by_id(self.repo.actors())

    def get_requestor(self):
        return self.repo.requestor()

    def get_all_but_requestor(self):
        results = filter(lambda a: a.id != self.repo.requestor_id, self.repo.actors())
        return self._sort_by_id(results)

    def get_adjacent_actors(self, target_actor):
        actors = self.repo.actors()
        results = []
        for a in actors:
            proximate_column = abs(a.student.seat.column - target_actor.student.seat.column) <= 1
            proximate_row = abs(a.student.seat.row - target_actor.student.seat.row) <= 1
            if proximate_column and proximate_row and (proximate_column + proximate_row) > 0:
                results.append(a)
        return self._sort_by_id(results)

    def set_grades(self, actor, value):
        operation = self._build_mod_attribute_operation(actor, value, OperatorType.Set, tags={Tag.Grades})
        self.program_api.actors.set_grades(operation=operation)

    def add_grades(self, actor, value):
        operation = self._build_mod_attribute_operation(actor, value, OperatorType.Add, tags={Tag.Grades})
        self.program_api.actors.add_grades(operation=operation)

    def subtract_grades(self, actor, value):
        operation = self._build_mod_attribute_operation(actor, value, OperatorType.Subtract, tags={Tag.Grades})
        self.program_api.actors.subtract_grades(operation=operation)

    def set_popularity(self, actor, value):
        operation = self._build_mod_attribute_operation(actor, value, OperatorType.Set, tags={Tag.Popularity})
        self.program_api.actors.set_popularity(operation=operation)

    def add_popularity(self, actor, value):
        operation = self._build_mod_attribute_operation(actor, value, OperatorType.Add, tags={Tag.Popularity})
        self.program_api.actors.add_popularity(operation=operation)

    def subtract_popularity(self, actor, value):
        operation = self._build_mod_attribute_operation(actor, value, OperatorType.Subtract, tags={Tag.Popularity})
        self.program_api.actors.subtract_popularity(operation=operation)

    def set_trouble(self, actor, value):
        operation = self._build_mod_attribute_operation(actor, value, OperatorType.Set, tags={Tag.Trouble})
        self.program_api.actors.set_trouble(operation=operation)

    def add_trouble(self, actor, value):
        operation = self._build_mod_attribute_operation(actor, value, OperatorType.Add, tags={Tag.Trouble})
        self.program_api.actors.add_trouble(operation=operation)

    def subtract_trouble(self, actor, value):
        operation = self._build_mod_attribute_operation(actor, value, OperatorType.Subtract, tags={Tag.Trouble})
        self.program_api.actors.subtract_trouble(operation=operation)

    def set_torment(self, actor, value):
        operation = self._build_mod_attribute_operation(actor, value, OperatorType.Set, tags={Tag.Torment})
        self.program_api.actors.set_torment(operation=operation)

    def add_torment(self, actor, value):
        operation = self._build_mod_attribute_operation(actor, value, OperatorType.Add, tags={Tag.Torment})
        self.program_api.actors.add_torment(operation=operation)

    def subtract_torment(self, actor, value):
        operation = self._build_mod_attribute_operation(actor, value, OperatorType.Subtract, tags={Tag.Torment})
        self.program_api.actors.subtract_torment(operation=operation)

    def refresh_hand(self, actor):
        # TODO: should this be an operation or does it not matter?
        self.program_api.actors.refresh_hand(actor.id)

    def _build_mod_attribute_operation(self, actor, value, operator, tags=None):
        # TODO: backwards compat until Add tag is phased out for subtract operations
        if operator == OperatorType.Add and value < 0:
            operator = OperatorType.Subtract
            value *= -1

        default_tags = self.repo.default_tags
        return ModifyAttribute(
            operator=operator,
            value=value,
            targeted_actor_id=actor.id,
            tags=default_tags.union(tags or set())
        )

    def _sort_by_id(self, actors):
        return list(sorted(actors, key=lambda actor: actor.id))
