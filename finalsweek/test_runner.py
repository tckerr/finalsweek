from datetime import datetime

from rest_framework.test import APIClient

from ai.interface_ai import AiActor
from trace.logger import Logger, register_exit_hook
from trace.definitions import LogLevel, LogType
from util.random import choice


class FinalsweekClient(object):
    def __init__(self) -> None:
        super().__init__()
        self.api_client = APIClient()

    def create(self, player_count):
        endpoint = "/api/games/"
        data = {"player_count": player_count}
        return self._post(data, endpoint)

    def load(self, game_id, actor_id, fresh=False):
        endpoint = "/api/games/{game_id}".format(game_id=game_id)
        data = {"actor_id": actor_id, "fresh": fresh}
        return self._get(data, endpoint)

    def take_turn(self, game_id, actor_id, action):
        endpoint = "/api/activities/"
        data = {
            "actor_id": actor_id,
            "game_id": game_id,
            "action_params": action
        }
        return self._post(data, endpoint)

    # private

    def _post(self, data, endpoint):
        return self._exec_method(self.api_client.post, endpoint, data)

    def _get(self, data, endpoint):
        return self._exec_method(self.api_client.get, endpoint, data)

    def _exec_method(self, method, endpoint, data):
        response = method(endpoint, data, format="json")
        if response.status_code in (301, 302):
            return self._exec_method(method, response.url, data)
        return response.data


class TestRunner(object):
    def __init__(self):
        super().__init__()
        self.api_client = FinalsweekClient()

    def run_load_test(self, game_id, actor_id):
        start = datetime.utcnow()
        digest = self.interface.load(game_id, actor_id)
        self.execute(digest, start)

    def run_create_test(self, player_count):
        start = datetime.utcnow()
        response = self.api_client.create(player_count)
        self.execute(response, start)

    def execute(self, data, start):
        register_exit_hook(data["public"]["game_id"])
        if not data["complete"]:
            actors = self.__generate_actors(data)
            Logger.log("Starting game", data["public"]["game_id"], level=LogLevel.Info, log_type=LogType.TestRunner)
            actor = choice(actors)
            while True:
                actor_id = actor.take_turn_if_possible()
                if not actor_id:
                    break
                actor = self.get_actor_by_id(actor_id, actors)
        elapsed = datetime.utcnow() - start
        complete_msg = "Done! Game ID: {}".format(data["public"]["game_id"])
        Logger.log(complete_msg, level=LogLevel.Info, log_type=LogType.TestRunner)
        performance_msg = "Processing took {}s".format(elapsed.total_seconds())
        Logger.log(performance_msg, level=LogLevel.Info, log_type=LogType.TestRunner)

    def __generate_actors(self, data):
        game_actors = data["public"]["actors"]
        return [AiActor(actor["id"], data["public"]["game_id"], actor["label"], self.api_client) for actor in
                game_actors]

    @staticmethod
    def get_actor_by_id(actor_id, actors):
        for actor in actors:
            if actor.id == actor_id:
                return actor
