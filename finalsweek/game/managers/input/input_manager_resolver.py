from game.managers.input.accumulation_input_manager import AccumulationInputManager
from game.managers.input.classtime_input_manager import ClasstimeInputManager
from game.managers.input.input_manager_base import InputManagerBase

class InputManagerResolver(object):

    def __init__(self):
        self.phase_type_managers = {
            "Accumulation": AccumulationInputManager(),
            "Classtime": ClasstimeInputManager(),            
        }

    def resolve(self, turn, action):
        phase_type_id = turn.phase.phase_type_id
        if phase_type_id in self.phase_type_managers:
            return self.phase_type_managers[phase_type_id].input(turn, action)
        else:
            # temporary until i build em all
            InputManagerBase().input(turn, action)