from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .forms import Lin
from .models import Link


class LinkListView(View):
    model = Link

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['links'] = request.user.profile.link_set
        return context


class CreateLinkView(CreateView):
    form_class = LinkForm
    success_url = reverse_lazy('link-list')