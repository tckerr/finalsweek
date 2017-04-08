from game.models import Instruction
from game.resolvers import OperatorResolver

class OperationApplier(object):
    def __init__(self):
        self.operator_resolver = OperatorResolver()

    # TODO RENAME KEYS
    def apply(self, decisions):
        targets = decisions["target_choices"]
        operation_set_results = decisions["operation_set_choices"]

        for instruction_id, operation_results in operation_set_results.items():
            kwargs = {}
            for arg_key, argument_result in operation_results.items():
                kwargs[arg_key] = argument_result
            # we have to go back for the operator
            instruction = Instruction.objects.get(pk=instruction_id)
            operator_fn = self.operator_resolver.resolve(instruction.operator_id)
            for target in targets:
                operator_fn(target, instruction.target_field, **kwargs)