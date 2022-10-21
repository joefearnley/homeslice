from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from accounts.views import AccountViewSet, AccountSignupView

router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/signup/', AccountSignupView.as_view(), name='signup')
]
