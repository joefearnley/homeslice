from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from accounts import views

router = routers.DefaultRouter()
router.register(r'accounts', views.AccountViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
