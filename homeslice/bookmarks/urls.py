from django.urls import path
from .views import BookmarkListView, BookmarkAddView

# BookmarkUpdateView, BookmarkDeleteView

urlpatterns = [
    path('', BookmarkListView.as_view(), name='bookmark_list'),
    path('add', BookmarkAddView.as_view(), name='bookmark_add'),
#    path('edit/<int:pk>', BookmarkUpdateView.as_view(), name='bookmark_edit'),
#    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='bookmark_delete'),
]