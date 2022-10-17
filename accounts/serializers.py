from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = [
            'url', 'username', 'email', 
            'first_name','last_name',
            'is_staff', 'is_active', 'date_joined'
        ]

