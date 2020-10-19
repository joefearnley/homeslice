from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('email','password1','password2',)
        # error_messages = {
        #     'email': {
        #         'required': 'Please enter a valid Email address',
        #         'unique': 'This email address is already registered',
        #     },
        #     'password1': {
        #         'required': 'Please enter a password',
        #     },
        #     'password2': {
        #         'required': 'Please enter a password confirmation',
        #     },
        # },
        help_texts = {
            'password1': 'Please enter a password',
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['email'].label = 'Email Address'
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'

    def save(self):
        user = super(SignUpForm, self).save(commit=False)
        user.username = self.cleaned_data['email']
        user.email = self.cleaned_data['email']
        user.save()
        return user


class LoginForm(forms.Form):
    class Meta:
        model = User
        fields = ('email', 'password',)
