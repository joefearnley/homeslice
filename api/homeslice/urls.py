from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from accounts.views import AccountViewSet, AccountSignUpAPIView, LogoutAPIView, UpdatePasswordAPIView

router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/signup/', AccountSignUpAPIView.as_view(), name='signup'),
    path('api/v1/login/', obtain_auth_token, name='login'),
    path('api/v1/logout/', LogoutAPIView.as_view(), name='logout'),
    path('api/v1/account/update-password', UpdatePasswordAPIView.as_view(), name='update-password'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
