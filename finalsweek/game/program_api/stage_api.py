from datetime import datetime

from game.scripting.api.program_child_api import ProgramChildApi


class StageApi(ProgramChildApi):
    def list_stages(self):
        return self.data.gameflow.stages

    def create_stage(self, stage_type):
        return self.data.gameflow.add_stage(stage_type)

    def complete_stage(self, stage_id):
        for stage in self.data.gameflow.stages:
            if stage.id == stage_id:
                stage.completed = datetime.utcnow()
                return
