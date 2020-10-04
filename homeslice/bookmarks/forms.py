from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Bookmark


class BookmarkCreateForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ['name', 'url', 'notes']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'url': forms.URLInput(attrs={'class': 'appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'notes': forms.Textarea(attrs={'class': 'appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'})
        }
        labels = {
            'name': _('Writer'),
            'url': 'URL',
            'notes': 'Notes'
        }

