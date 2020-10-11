from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Bookmark
from .forms import BookmarkForm, BookmarkUpdateForm


class BookmarkListView(LoginRequiredMixin, ListView):
    model = Bookmark
    template_name = 'list.html'
    context_object_name = 'bookmarks'

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user).order_by('-created_date')


class BookmarkCreateView(CreateView):
    template_name = 'form.html'
    model = Bookmark
    form_class = BookmarkForm
    success_url = reverse_lazy('bookmark_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BookmarkCreateView, self).form_valid(form)


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    template_name = 'form.html'
    form_class = BookmarkForm
    success_url = reverse_lazy('bookmark_list')


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark_list')
