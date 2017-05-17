from game.document.documents.prompt import Prompt
from game.gameflow.actions.script_card_action import ScriptCardAction
from game.scripting.discipline_card_script_runner import DisciplineCardScriptRunner


class DisciplineAction(ScriptCardAction):
    def __init__(self, data) -> None:
        super().__init__(data)
        self.prompt = Prompt(data["prompt"])

    def _get_card(self, actor_id, api):
        # TODO: check if fresh is needed
        turn = self._get_current_turn(actor_id, api)
        return api.game_decks.get_discipline_card_for_phase(turn.phase.id)

    def _run_script(self, actor_id, api, script):
        discipline_card_script_runner = DisciplineCardScriptRunner(actor_id, self.prompt)
        return discipline_card_script_runner.run(api, script)

    # TODO: there's some duplication between this class and ActionCardAction
    # TODO: discipline cards should probably get transferred into the board's "in play" hand
    def _resolve_completion(self, actor_id, api, card, result):
        if card.generates_mutation:
            self.card_mutation_generator.generate_without_transfer(actor_id, api, card, result)

    @staticmethod
    def _get_current_turn(actor_id, api):
        turn = api.turns.get_or_create_current_turn()
        assert turn.actor_id == actor_id
        return turn
