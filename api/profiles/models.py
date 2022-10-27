from django.db import models
from accounts.models import Account


class Profile(models.Model):
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100)
    username  = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)


class Link(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
    url = models.CharField(max_length=30, blank=False)
    title = models.CharField(max_length=30, blank=False)
    is_active = models.BooleanField(default=True)
