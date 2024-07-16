from django.urls import path
from .views import BookmarkListCreateView, BookmarkRetrieveDestroyView

urlpatterns = [
    path('', BookmarkListCreateView.as_view(), name='bookmark-list-create'),
    path(
        '<int:pk>/',
        BookmarkRetrieveDestroyView.as_view(),
        name='bookmark-detail',
    ),
]
