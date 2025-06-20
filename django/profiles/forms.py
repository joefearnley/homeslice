from django import forms
from .models import Link


class LinkForm(forms.ModelForm):

    class Meta:
        model = Link
        fields = ['url', 'title', 'is_active']

        widgets = {
            'url': forms.URLInput(),
            'title': forms.TextInput(),
            'is_active': forms.CheckboxInput(),
        }
