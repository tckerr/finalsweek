from rest_framework import routers
#
from viewsets import GameViewSet

router = routers.DefaultRouter()
router.register(r'games', GameViewSet)
