from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Bookmark


class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ['name', 'url', 'notes']
        labels = {
            'name': _('Name'),
            'url': _('URL'),
            'notes': _('Notes')
        }
        help_texts = {
            'name': 'Please enter a name.',
            'url': 'Please enter a valid URL.'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'url': forms.URLInput(attrs={'class': 'appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'notes': forms.Textarea(attrs={
                'class': 'appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'rows': 4,
                'cols': 10
            })
        }


class BookmarkUpdateForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ['name', 'url', 'notes']
        labels = {
            'name': _('Name'),
            'url': _('URL'),
            'notes': _('Notes')
        }
        help_texts = {
            'name': 'Please enter a name.',
            'url': 'Please enter a valid URL.'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'url': forms.URLInput(attrs={'class': 'appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'notes': forms.Textarea(attrs={
                'class': 'appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'rows': 4,
                'cols': 10
            })
        }
