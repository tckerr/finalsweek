class ProgramChildApi(object):
    def __init__(self, program_api) -> None:
        super().__init__()
        self.program_api = program_api

    @property
    def data(self):
        return self.program_api.data
