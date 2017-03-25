from django.conf.urls import url, include
from django.contrib import admin
from api.routes import router as api_router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_router.urls))
]
