from django import forms
from .models import Link


class LinkForm(forms.ModelForm):

    def save(self, commit=True):
        instance = super(LinkForm, self).save(commit=False)

        instance.profile = self.user

        if commit:
            instance.save(), 

        return instance

    class Meta:
        model = Link
        fields = ['url', 'title', 'is_active']

        widgets = {
            'url': forms.URLInput(),
            'title': forms.TextInput(),
            'is_active': forms.CheckboxInput(),
        }
