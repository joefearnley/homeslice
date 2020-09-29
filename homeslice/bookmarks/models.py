from django.db import models
from django.contrib.auth.models import User

class Bookmark(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=150)
    url = models.CharField(max_length=100)
    notes = models.CharField(max_length=256, null=True, blank=True)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

class Tag(models.Model):
    name = models.CharField(max_length=150)
    bookmark = models.ForeignKey(Bookmark, on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
