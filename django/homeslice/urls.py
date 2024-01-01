from django.contrib import admin
from django.urls import include, path
from .views import HomeView, DashboardView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('', DashboardView.as_view(), name='dashboard'),
    path('admin/', admin.site.urls),

    # include api urls
]
