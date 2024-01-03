from django.contrib import admin
from django.urls import include, path
from .views import HomeView, DashboardView
from accounts.views import SignupView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('admin/', admin.site.urls),

    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    # include api urls
]
