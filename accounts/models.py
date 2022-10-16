from django.db import models
from django.contrib.auth.admin import User


class Account(User):

    class Meta:
        proxy = True
