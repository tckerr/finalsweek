from util.random import random_id


class PhaseSeedFactory(object):
    @staticmethod
    def create(phase_type, mutations=None):
        return {
            "id":         random_id(),
            "phase_type": phase_type,
            "completed":  None,
            "turns":      [],
            "mutations":  mutations or []
        }
