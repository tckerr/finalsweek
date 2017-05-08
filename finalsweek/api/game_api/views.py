from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from game.document.persistence.connectors import GameDbConnector
from game.gameflow.actions.action_card import ActionCardAction
from game.gameflow.actions.base import ActionBase
from game.gameflow.actions.discipline import DisciplineAction
from game.interface.game_interface import GameInterface


# TODO: its own class
def get_action_cls(action):
    action_type = action.get("type", None)
    if action_type == "DisciplineAction":
        return DisciplineAction
    elif action_type == "ActionCardAction":
        return ActionCardAction
    else:
        return ActionBase


class GameInterfaceViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.interface = GameInterface()

    @staticmethod
    def _serialize(digest):
        return digest.data

    @staticmethod
    def get_param(request, key):
        if key not in request.query_params:
            raise ValidationError("You must supply the '{}' parameter.".format(key))
        return request.query_params.get(key)

    @staticmethod
    def get_post_data(request, key,):
        if key not in request.data:
            raise ValidationError("You must supply the '{}' parameter.".format(key))
        return request.data[key]


class GameViewSet(GameInterfaceViewSet):
    def create(self, request):
        player_count = self.get_post_data(request, "player_count")
        digest = self.interface.create(player_count)
        return Response(self._serialize(digest))

    def list(self, request):
        db = GameDbConnector()
        ids = db.list_summaries()
        return Response(ids)

    def retrieve(self, request, pk=None, actor_id=None):
        fresh = self.request.query_params.get("fresh", False)
        actor_id = self.get_param(request, "actor_id")
        digest = self.interface.load(pk, actor_id, fresh=fresh)
        return Response(self._serialize(digest))


class ActivityViewSet(GameInterfaceViewSet):
    def create(self, request):
        actor_id = self.get_post_data(request, "actor_id")
        game_id = self.get_post_data(request, "game_id")
        action_params = self.get_post_data(request, "action_params")
        action_cls = get_action_cls(action_params)
        digest = self.interface.take_turn(game_id, actor_id, action_cls(action_params))
        return Response(self._serialize(digest))
