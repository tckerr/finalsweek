from rest_framework import routers

#
from api.game_api.views import GameViewSet, ActivityViewSet
from api.model_apis.users.routes import router as user_router
from api.routing.RouteRegister import RouteRegister

router = routers.DefaultRouter()
route_register = RouteRegister()

route_register.RegisterAll(user_router, router)
router.register(base_name="games", prefix="games", viewset=GameViewSet)
router.register(base_name="activities", prefix="activities", viewset=ActivityViewSet)
