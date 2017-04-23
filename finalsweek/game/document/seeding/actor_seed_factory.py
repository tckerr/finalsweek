from random import shuffle, choice

from util import guid


class StudentSeedFactory(object):

    def create(self, student_infos, as_actor=False):
        student_info_id = choice(student_infos)["id"]
        actor = self._actor() if as_actor else None
        return {
            "id":              guid(),
            "student_info_id": student_info_id,
            "actor":           actor
        }
