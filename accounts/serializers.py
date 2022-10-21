from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Account

class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = [
            'url', 'username', 'email', 
            'first_name','last_name',
            'is_staff', 'is_active', 'date_joined'
        ]


class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['username', 'email', 'password']

    def signup(self, validated_data):
        account = Account.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        account.set_password(validated_data['password'])
        account.save()

        return account


class LoginSerilizer(serializers.Serializer):
    pass