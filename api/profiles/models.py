from django.db import models
from accounts.models import Account


class Profile(models.Model):
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Link(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
    url = models.CharField(max_length=30, blank=False)
    title = models.CharField(max_length=30, blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{} | {}'.format(self.title, self.url)
