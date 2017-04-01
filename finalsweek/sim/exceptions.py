class CustomException(Exception):
    def __init__(self, message, errors):
        super(CustomException, self).__init__(message)
        # custom code...

class NotImplementedException(CustomException): pass
class RulesViolation(CustomException): pass