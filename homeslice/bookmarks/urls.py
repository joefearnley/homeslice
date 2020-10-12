from django.urls import path
from .views import BookmarkListView, BookmarkCreateView, BookmarkUpdateView, BookmarkDeleteView

urlpatterns = [
    path('', BookmarkListView.as_view(), name='bookmark_list'),
    path('add', BookmarkCreateView.as_view(), name='bookmark_create'),
    path('edit/<int:pk>', BookmarkUpdateView.as_view(), name='bookmark_update'),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='bookmark_delete'),
]