from sim.messages.message_types import MessageTypes

class Component(object):
    # overwrite me
    def receive_message(self, message_type, data):
        pass


class IntegerComponent(Component):

    def __init__(self, *args, **kwargs):
        self.__value = 0
        super(IntegerComponent, self).__init__(*args, **kwargs)

    def add(self, value):
        self.__value += value

    def remove(self, value):
        self.add(-1 * value)

    @property
    def value(self):
        return self.__value


class GradesComponent(IntegerComponent):
    def receive_message(self, message_type, data):
        if message_type is MessageTypes.GradesModification:
            self.add(data["value"])

        if message_type is MessageTypes.ReportGrades:
            print self.value

class PopularityComponent(IntegerComponent): pass
class TurnComponent(Component): pass
