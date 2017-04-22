from random import choice

from django.core.management.base import BaseCommand

from ai.interface_ai import AiActor
from game.interface.game_interface import GameInterface


class Command(BaseCommand):
    def __init__(self, stdout=None, stderr=None, no_color=False):
        super().__init__(stdout, stderr, no_color)
        self.previously_chosen_card = None
        self.interface = GameInterface()

    def handle(self, *args, **options):
        digest = self.interface.create(4)
        # digest = self.interface.load("58fbb349529bc21b9c3f9fd2", "227d0d2e-50a5-4d3f-80d3-af883e549a7e")
        if not digest.complete:
            actors = self.__generate_actors(digest)
            print("Starting game", digest.game_info.game_id)

            actor = choice(actors)
            while True:
                actor_id = actor.take_turn_if_possible()
                if not actor_id:
                    break
                actor = self.get_actor_by_id(actor_id, actors)

        print("Done! Game ID: {}".format(digest.game_info.game_id))

    def __generate_actors(self, digest):
        game_actors = digest.game_info.actors
        return [AiActor(actor.id, digest.game_info.game_id, self.interface) for actor in game_actors]

    @staticmethod
    def get_actor_by_id(actor_id, actors):
        for actor in actors:
            if actor.id == actor_id:
                return actor
