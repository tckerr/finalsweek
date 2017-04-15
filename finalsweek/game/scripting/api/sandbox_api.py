class SandboxApi(object):
    def __init__(self, save_queue, repository):
        self.save_queue = save_queue
        self.repo = repository