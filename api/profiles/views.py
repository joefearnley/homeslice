from rest_framework import views, viewsets, permissions, status, generics
from .serilizers import ProfileSerializer
from .models import Profile, Link


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows CRUD operations on Profiles.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(account=self.request.user)
