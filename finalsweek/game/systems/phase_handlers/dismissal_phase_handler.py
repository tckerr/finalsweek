from game.configuration.definitions import OperatorType, Tag
from game.operation.operations.modify_attribute import ModifyAttribute
from game.scripting.discipline_card_script_runner import DisciplineCardScriptRunner
from game.systems.phase_handlers.phase_handler_base import PhaseHandlerBase


class DismissalPhaseHandler(PhaseHandlerBase):
    def __init__(self, api):
        super().__init__(api)
        self.discipline_card_script_runner = DisciplineCardScriptRunner()

    def on_create(self, phase):
        super().on_create(phase)
        discipline_card = self.api.game_decks.set_discipline_card_for_phase(phase)
        self.discipline_card_script_runner.run(self.api, discipline_card.template.script)

    def on_complete(self, phase):
        self.clear_trouble()
        super().on_complete(phase)

    def clear_trouble(self):
        for actor in self.api.actors.list():
            operation = ModifyAttribute(
                operator=OperatorType.Set,
                value=0,
                targeted_actor_id=actor.id,
                tags={Tag.System, Tag.Trouble})
            self.api.actors.set_trouble(operation=operation)
