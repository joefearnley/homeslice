from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView, DashboardView
from accouts.views import AccountSettingsView
from allauth.account.views import signup, login, logout

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('signup/', signup, name='allauth_signup'),
    path('login/', login, name='allauth_login'),
    path('logout/', logout, name='allauth_logout'),

    path('accounts/', include('allauth.urls')),

    path('my-account/', AccountSettingsView.as_view(), name='my-account'),

    # include api urls
]
