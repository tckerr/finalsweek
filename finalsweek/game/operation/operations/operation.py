class Operation(object):
    def __init__(self, operation_type, tags: list) -> None:
        super().__init__()
        self.operation_type = operation_type
        self.tags = list(tags)
        self.targeted_actor_id = None