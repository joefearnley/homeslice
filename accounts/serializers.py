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


class SignupSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=Account.objects.all())]
    )

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Account.objects.all())]
    )

    class Meta:
        model = Account
        fields = ['username', 'email', 'password']

    def signup(self, validated_data):
        account = Account.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        account.set_password(validated_data['password'])
        account.save()

        return account


class LoginSerilizer(serializers.Serializer)
    pass