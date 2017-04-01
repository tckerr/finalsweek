from rest_framework import routers
#
from api.model_apis.users.viewsets import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
