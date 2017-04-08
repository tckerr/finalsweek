from game.models import Operation
from game.resolvers import OperatorResolver

class OperationApplier(object):
    def __init__(self):
        self.operator_resolver = OperatorResolver()

    # TODO RENAME KEYS
    def apply(self, decisions):
        targets = decisions["target_choices"]
        operation_set_results = decisions["operation_set_choices"]

        for operation_id, operation_results in operation_set_results.items():
            kwargs = {}
            for arg_key, argument_result in operation_results.items():
                kwargs[arg_key] = argument_result
            # we have to go back for the operator
            operation = Operation.objects.get(pk=operation_id)
            operator_fn = self.operator_resolver.resolve(operation.operator_id)
            for target in targets:
                operator_fn(target, operation.target_field, **kwargs)