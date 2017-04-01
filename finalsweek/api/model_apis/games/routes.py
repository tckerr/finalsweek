from rest_framework import routers
#
from api.model_apis.games.viewsets import GameViewSet

router = routers.DefaultRouter()
router.register(r'games', GameViewSet)
