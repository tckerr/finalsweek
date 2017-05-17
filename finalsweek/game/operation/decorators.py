from game.exceptions import OperationException


def get_operation(kwargs):
    operation = kwargs.get("operation", None)
    if not operation:
        raise OperationException("Operation receiver received no operation. Did you pass it as a named parameter?")
    return operation


def accepts_operation(*operation_types):
    def _accepts_operation_wrapper(func):
        def __fw_operation_receiver__(*args, **kwargs):
            operation = get_operation(kwargs)
            operation_type = operation.operation_type
            if operation_type not in operation_types:
                raise OperationException("Invalid operation '{}' passed to operation receiver.".format(operation_type))
            return func(*args, **kwargs)

        return __fw_operation_receiver__

    return _accepts_operation_wrapper


def accepts_operator(*operator_types):
    def _accepts_operator_wrapper(func):
        def __fw_operation_receiver__(*args, **kwargs):
            operation = get_operation(kwargs)
            operator = operation.operator
            if operator not in operator_types:
                raise OperationException("Invalid operator '{}' passed to operation receiver.".format(operator))
            return func(*args, **kwargs)

        return __fw_operation_receiver__

    return _accepts_operator_wrapper
