from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Bookmark
from .forms import BookmarkAddForm


class BookmarkListView(LoginRequiredMixin, ListView):
    model = Bookmark
    template_name = 'list.html'
    context_object_name = 'bookmarks'
    ordering = ['-created_date']

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user)


class BookmarkAddView(CreateView):
    template_name = 'add.html'
    model = Bookmark
    form_class = BookmarkAddForm
    success_url = reverse_lazy('bookmark_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BookmarkAddView, self).form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     print('Get post req')
    #     # form = self.form_class
    #     # if form.is_valid():
    #     #     print('Valid form')
    #     #     return 'Success'
    #     return 'failed'

# class BookmarkUpdateView(UpdateView):
#     model = Bookmark
#     fields = ['name', 'pages']
#     success_url = reverse_lazy('bookmark_list')

# class BookmarkDeleteView(DeleteView):
#     model = Bookmark
#     success_url = reverse_lazy('bookmark_list')
