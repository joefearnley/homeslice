from django import forms
from .models import Link


class LinkForm(forms.ModelForm):

    def save(self, commit=True):
        instance = super(LinkForm, self).save(commit=False)

        profile_id = self.data.get('profile_id')

        instance.profile_id = self.user

        if commit:
            instance.save(), 

        return instance

    class Meta:
        model = Link
        fields = ['profile', 'url', 'title', 'is_active']

        widgets = {
            'profile': forms.HiddenInput(),
            'url': forms.URLInput(),
            'title': forms.TextInput(),
            'is_active': forms.CheckboxInput(),
        }