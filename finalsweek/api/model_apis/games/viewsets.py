from rest_framework import viewsets
from rest_framework import permissions
from sim.models import Game
#
from api.model_apis.games.serializers import GameSerializer

class GameViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.IsAuthenticated,)
	queryset = Game.objects.all()
	serializer_class = GameSerializer
