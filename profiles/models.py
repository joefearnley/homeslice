from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    username  = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    active = models.BooleanField(default=True)


class Link(models.Model):
    profile = models.ForeignKey(
        'Profile',
        on_delete=models.CASCADE,
    )
    url = models.CharField(max_length=30, blank = False)
    title = models.CharField(max_length=30, blank = False)
    active = models.BooleanField(default=True)
