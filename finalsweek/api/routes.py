from rest_framework import routers

#
from api.model_apis.users.routes import router as user_router
from api.routing.RouteRegister import RouteRegister

router = routers.DefaultRouter()
route_register = RouteRegister();

route_register.RegisterAll(user_router, router)
