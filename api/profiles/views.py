from rest_framework import viewsets, permissions
from .serilizers import ProfileSerializer, LinkSerializer
from .models import Profile, Link


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows CRUD operations on Profiles.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(account=self.request.user)

    def perform_update(self, serializer):
        serializer.save(account=self.request.user)


class LinkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows CRUD operations on Profile Links.
    """
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        profile = Profile.objects.get(account=self.request.user)
        return self.queryset.filter(profile=profile)

    def perform_create(self, serializer):
        profile = Profile.objects.get(account=self.request.user)
        serializer.save(profile=profile)

    def perform_update(self, serializer):
        profile = Profile.objects.get(account=self.request.user)
        serializer.save(profile=profile)
