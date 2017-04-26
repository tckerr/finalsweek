from game.operation.operation import ModifyAttribute, OperatorType
from game.scripting.api.sandbox_api import SandboxApi


class ActorApi(SandboxApi):
    # TODO: merge with program API
    def __init__(self, *args, **kwargs):
        super(ActorApi, self).__init__(*args, **kwargs)

    def get_actors(self):
        return self.repo.actors()

    def get_requestor(self):
        return self.repo.requestor()

    def get_all_but_requestor(self):
        return list(filter(lambda a: a.id != self.repo.requestor_id, self.repo.actors()))

    def get_adjacent_actors(self, target_actor):
        actors = self.repo.actors()
        results = []
        for a in actors:
            proximate_column = abs(a.student.seat.column - target_actor.student.seat.column) <= 1
            proximate_row = abs(a.student.seat.row - target_actor.student.seat.row) <= 1
            if proximate_column and proximate_row and (proximate_column + proximate_row) > 0:
                results.append(a)
        return results

    def set_grades(self, actor, value):
        operation = self._build_mod_attribute_operation(actor, value, OperatorType.Set)
        self.program_api.actors.set_grades(operation=operation)

    def add_grades(self, actor, value):
        operation = self._build_mod_attribute_operation(actor, value, OperatorType.Add)
        self.program_api.actors.add_grades(operation=operation)

    def set_popularity(self, actor, value):
        operation = self._build_mod_attribute_operation(actor, value, OperatorType.Set)
        self.program_api.actors.set_popularity(operation=operation)

    def add_popularity(self, actor, value):
        operation = self._build_mod_attribute_operation(actor, value, OperatorType.Add)
        self.program_api.actors.add_popularity(operation=operation)

    def set_trouble(self, actor, value):
        operation = self._build_mod_attribute_operation(actor, value, OperatorType.Set)
        self.program_api.actors.set_trouble(operation=operation)

    def add_trouble(self, actor, value):
        operation = self._build_mod_attribute_operation(actor, value, OperatorType.Add)
        self.program_api.actors.add_trouble(operation=operation)

    def set_torment(self, actor, value):
        operation = self._build_mod_attribute_operation(actor, value, OperatorType.Set)
        self.program_api.actors.set_torment(operation=operation)

    def add_torment(self, actor, value):
        operation = self._build_mod_attribute_operation(actor, value, OperatorType.Add)
        self.program_api.actors.add_torment(operation=operation)

    def _build_mod_attribute_operation(self, actor, value, operator):
        return ModifyAttribute(
            operator=operator,
            value=value,
            actor_id=actor.id,
            metadata=self.repo.metadata
        )
