from django import forms
from .models import Account


class UpdateAccountForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ['username', 'first_name', 'last_name', 'email']


class DeleteAccountForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ['id']
