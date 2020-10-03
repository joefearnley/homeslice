from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Bookmark
from .forms import BookmarkForm


class BookmarkListView(LoginRequiredMixin, ListView):
    model = Bookmark
    template_name = 'list.html'
    context_object_name = 'bookmarks'
    ordering = ['-created_date']

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user)


class BookmarkCreateView(CreateView):
    template_name = 'create.html'
    model = Bookmark
    fields = ['name', 'url']
    form = BookmarkForm()
    success_url = reverse_lazy('bookmark_list')

# class BookmarkUpdateView(UpdateView):
#     model = Bookmark
#     fields = ['name', 'pages']
#     success_url = reverse_lazy('bookmark_list')

# class BookmarkDeleteView(DeleteView):
#     model = Bookmark
#     success_url = reverse_lazy('bookmark_list')
