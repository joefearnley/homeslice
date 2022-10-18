from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager


class AccountManager(BaseUserManager):

    def create_user(self, username, name, password=None):
        if not email:
            raise ValueError('Account must have an email address')

        email = self.normalize_email(email)
        account = self.model(username=username, name=name)
        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, username, name, password):
        account = self.create_user(username, name, password)
        account.is_superuser = True
        account.is_staff = True
        account.save()

        return account


class Account(AbstractUser, PermissionsMixin):

    email = models.EmailField(max_length=255, unique=True)
    username = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = AccountManager()

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email
