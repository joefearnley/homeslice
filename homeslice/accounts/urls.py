from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from .views import UserLoginView #, RegisterView

urlpatterns = [
    url('login/', UserLoginView.as_view(), name='login'),
    #url(r'^register/', RegisterView.as_view(), name='register'),
]