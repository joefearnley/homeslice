from django import forms
from .models import Account


class UpdateAccountForm(forms.Form):

    class Meta:
        model = Account


class DeleteAccountForm(forms.Form):
    pass

