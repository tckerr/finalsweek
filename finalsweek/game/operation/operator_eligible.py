class OperationException(Exception):
    pass


def receives_operation(func):
    func.__operation = True

    def __fw_operation__(*args, **kwargs):
        metadata = kwargs.pop("metadata", None)
        result = func(*args, **kwargs)
        if not metadata: pass
            #print("Warning: no metadata supplied to a method that is marked as '@receives_operation'.")
        #print(metadata, result)
        return result

    return __fw_operation__
