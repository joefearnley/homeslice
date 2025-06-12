from django.db import models
from accounts.models import Account


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Profile(TimeStampMixin):
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Link(TimeStampMixin):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
    url = models.URLField(blank=False)
    title = models.CharField(max_length=250, blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{} | {}'.format(self.title, self.url)
