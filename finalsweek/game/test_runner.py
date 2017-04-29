from datetime import datetime

from ai.interface_ai import AiActor
from game.configuration.definitions import LogLevel, LogType
from game.interface.game_interface import GameInterface
from logger import Logger, register_exit_hook
from util.random import choice


class TestRunner(object):
    def __init__(self):
        super().__init__()
        self.interface = GameInterface()

    def run_load_test(self, game_id, actor_id):
        start = datetime.utcnow()
        digest = self.interface.load(game_id, actor_id)
        self.execute(digest, start)

    def run_create_test(self, player_count):
        start = datetime.utcnow()
        digest = self.interface.create(player_count)
        self.execute(digest, start)

    def execute(self, digest, start):
        register_exit_hook(str(digest.game_info.game_id))
        if not digest.complete:
            actors = self.__generate_actors(digest)
            Logger.log("Starting game", digest.game_info.game_id, level=LogLevel.Info, log_type=LogType.TestRunner)
            actor = choice(actors)
            while True:
                actor_id = actor.take_turn_if_possible()
                if not actor_id:
                    break
                actor = self.get_actor_by_id(actor_id, actors)
        elapsed = datetime.utcnow() - start
        complete_msg = "Done! Game ID: {}".format(digest.game_info.game_id)
        Logger.log(complete_msg, level=LogLevel.Info, log_type=LogType.TestRunner)
        performance_msg = "Processing took {}s".format(elapsed.total_seconds())
        Logger.log(performance_msg, level=LogLevel.Info, log_type=LogType.TestRunner)

    def __generate_actors(self, digest):
        game_actors = digest.game_info.actors
        return [AiActor(actor.id, digest.game_info.game_id, self.interface, actor.label) for actor in game_actors]

    @staticmethod
    def get_actor_by_id(actor_id, actors):
        for actor in actors:
            if actor.id == actor_id:
                return actor
