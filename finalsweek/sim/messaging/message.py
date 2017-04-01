class Message(dict):
    def __init__(self):
        self.metadata = {}

class ValueMessage(Message):
    """docstring for ValueMessage"""
    def __init__(self, value):
        super(ValueMessage, self).__init__()
        self["value"] = value
        