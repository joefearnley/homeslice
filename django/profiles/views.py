from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from accounts.models import Account
from profiles.models import Profile
from .forms import LinkForm
from .models import Link, Profile


class LinkListView(LoginRequiredMixin, ListView):
    model = Link
    template_name = 'profiles/links/index.html'

    def get_queryset(self, **kwargs):   
        return Link.objects.filter(profile=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        account = Account.objects.get(pk=self.request.user.pk)

        try:
            profile = Profile.objects.filter(account_id=account.pk).first()
        except Profile.DoesNotExist:
            profile = None

        try:
            links = Link.objects.filter(profile=profile)
        except Profile.DoesNotExist:
            links = None

        context['profile'] = profile
        context['links'] = links

        return context


class CreateLinkView(LoginRequiredMixin, CreateView):
    form_class = LinkForm
    template_name = 'profiles/links/create.html'
    success_url = reverse_lazy('link-list')
    success_message = _('Profile Link successfully created!')


class UpdateLinkView(LoginRequiredMixin, UpdateView):
    form_class = LinkForm
    template_name = 'profiles/links/update.html'
    success_url = reverse_lazy('link-list')
    success_message = _('Profile Link successfully updated!')


class DeleteLinkView(LoginRequiredMixin, DeleteView):
    model = Link
    success_url = reverse_lazy('link-list')
    success_message = _('Profile Link successfully delete!')