class MessageTypes(object):

    @classmethod
    def all_types(cls):
        msg_filter = lambda key: not key.startswith("__") and key is not "all"
        return ( key for key, value in cls.__dict__.items() if msg_filter(key) )

    GradesModification = "GradesModification"
    ReportGrades = "ReportGrades"
    UpdateGameslot = "UpdateGameslot"

    # DEBUGGING
    DebugEcho = "DebugEcho"
    DebugValues = "DebugValues"
