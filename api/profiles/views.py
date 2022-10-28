from rest_framework import views, viewsets, permissions, status, generics
from .serilizers import ProfileSerializer
from .models import Profile, Link


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows accounts to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
