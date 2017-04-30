class ListableClass(object):
    @classmethod
    def prop_list(cls):
        return [
            (getattr(cls, k), getattr(cls, k))
            for k in cls.__dict__
            if not k.startswith("__") and k is not "prop_list"]
