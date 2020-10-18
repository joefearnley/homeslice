from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class SignUpForm(forms.Form):
    email = forms.EmailField(required=True,)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    class Meta:
        fields = ['email', 'password',]
        labels = {
            'email': _('Emailsadfsasdf'),
            'password1': _('Pasfdafdsfassword'),
        }
        help_texts = {
            'email': 'Please enter a valid Email address',
            'password1': 'Please enter password',
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

    def save(self):
        user = super(SignUpForm, self).save(commit=False)
        user.username = self.cleaned_data['email']
        user.email = self.cleaned_data['email']
        user.save()
        return user


class LoginForm(forms.Form):
    class Meta:
        model = User
        fields = ('email', 'password')