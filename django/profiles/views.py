from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from accounts.models import Account
from profiles.models import Profile
from .forms import LinkForm
from .models import Link, Profile


class LinkListView(ListView):
    model = Link
    template = 'profiles/links.html'

    def get_queryset(self, **kwargs):
        return Link.objects.filter(profile=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        account = Account.objects.get(pk=self.request.user.pk)
        print(account.pk)
        
        profile = Profile.objects.get(account=account)


        
        # profile = account.profile
        # context['links'] = profile.link_set.all()
        return context


class CreateLinkView(CreateView):
    form_class = LinkForm
    success_url = reverse_lazy('link-list')
