from random import choice

from game.document.seeding.actor_seed_factory import ActorSeedFactory
from util import guid


class StudentSeedFactory(object):
    def __init__(self) -> None:
        super().__init__()
        self.actor_seed_factory = ActorSeedFactory()

    def create(self, student_info, as_actor=False):
        student_info_id = choice(student_info)["id"]
        actor = self.actor_seed_factory.create() if as_actor else None
        return {
            "id":              guid(),
            "student_info_id": student_info_id,
            "actor":           actor
        }
