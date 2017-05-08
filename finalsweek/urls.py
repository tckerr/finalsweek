from django.conf.urls import url, include
from django.contrib import admin
from rest_auth import urls as rest_auth_urls
from rest_auth.registration import urls as registration_urls
from api.routes import router as api_router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_router.urls)),
    url(r'^api/auth/', include(rest_auth_urls)),
    url(r'^api/auth/registration/', include(registration_urls)),
]
