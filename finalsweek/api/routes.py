from django.conf.urls import url, include
from rest_framework import routers
#
from api.model_apis.users.routes import router as user_router
from api.model_apis.games.routes import router as game_router
from api.routing.RouteRegister import RouteRegister

router = routers.DefaultRouter()
route_register = RouteRegister();

route_register.RegisterAll(user_router, router)
route_register.RegisterAll(game_router, router)