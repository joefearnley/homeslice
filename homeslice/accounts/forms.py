from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.Form):
    class Meta:
        model = User
        fields = ('email', 'password')

    def save(self, commit=True):
        user = super().save(False)
        user.email = user.username
        user = super().save()

        return user

class LoginForm(forms.Form):
    class Meta:
        model = User
        fields = ('email', 'password')