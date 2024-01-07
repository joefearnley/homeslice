from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView, DashboardView
from allauth.account.views import signup, login, logout

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    # path('signup/', SignupView.as_view(), name='signup'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('signup/', signup, name='allauth_signup'),
    path('login/', login, name='allauth_login'),
    path('logout/', logout, name='allauth_logout'),

    path('accounts/', include('allauth.urls')),

    path('admin/', admin.site.urls),


    # include api urls
]
