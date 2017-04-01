class CustomException(Exception):
    def __init__(self, message):
        super(CustomException, self).__init__(message)
        # custom code...

class NotImplementedException(CustomException): pass
class RulesViolation(CustomException): pass
class GameFlowViolation(CustomException): pass