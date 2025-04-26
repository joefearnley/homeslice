from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView, DashboardView
from accounts.views import AccountSettingsView, AccountUpateView
from profiles.views import LinkListView, CreateLinkView
from allauth.account.views import signup, login, logout
from api.urls import urlpatterns as api_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('signup/', signup, name='allauth_signup'),
    path('login/', login, name='allauth_login'),
    path('logout/', logout, name='allauth_logout'),

    path('accounts/', include('allauth.urls')),

    path('my-account/', AccountSettingsView.as_view(), name='my-account'),
    path('my-account/update', AccountUpateView.as_view(), name='update-my-account'),

    path('profile/links/', LinkListView.as_view(), name='link-list'),
    path('profile/links/create', CreateLinkView.as_view(), name='link-create'),
]

# include api urls 
urlpatterns += api_urlpatterns
