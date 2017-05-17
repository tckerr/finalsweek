from game.scripting.played_card_script_runner import PromptScriptRunner
from game.scripting.repositories import DisciplineCardScriptContextRepository


class DisciplineCardScriptRunner(PromptScriptRunner):
    def build_repo(self, api):
        return DisciplineCardScriptContextRepository(api, self.actor_id)