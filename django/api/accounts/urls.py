from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .accounts.views import AccountViewSet, AccountSignUpAPIView, LogoutAPIView, UpdatePasswordAPIView
from .profiles.views import ProfileViewSet, LinkViewSet

router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)

