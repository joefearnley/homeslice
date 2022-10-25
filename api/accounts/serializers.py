from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Account


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Account.objects.all())]
    )

    class Meta:
        model = Account
        fields = [
            'url', 'username', 'email', 
            'first_name','last_name',
            'is_staff', 'is_active', 'date_joined'
        ]


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'email': {'allow_null': False, 'allow_blank': False, 'required': True},
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        account = Account.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        account.set_password(validated_data['password'])
        account.save()

        return account

