from django.contrib.auth import password_validation
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from accounts.models import Account
from profiles.models import Profile


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

        # create a new profile on account creation
        Profile.objects.create(
            account=account,
            title=account.username,
        )

        return account


class UpdatePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = Account

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({'confirm_password': 'The two password fields did not match.'})

        password_validation.validate_password(data['password'], self.context['request'].user)
        return data

    def save(self):
        password = self.validated_data['password']
        account = self.context['request'].user
        account.set_password(password)
        account.save()
        return account
