from rest_framework import serializers
from profiles.models import Profile, Link


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['account', 'title', 'bio', 'is_active']


class LinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = ['url', 'title', 'is_active']
