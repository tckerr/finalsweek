from game.models import OperationModifier


class OperationModifierAdapter(object):
    @staticmethod
    def adapt(data):
        return {
            "id":     str(data.id),
            "script": data.script
        }


class OperationModifierSeedFactory(object):
    def __init__(self) -> None:
        super().__init__()
        self.operation_modifier_adapter = OperationModifierAdapter()

    def create(self, data):
        return self.operation_modifier_adapter.adapt(data)