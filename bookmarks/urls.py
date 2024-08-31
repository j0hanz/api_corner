from django.urls import path

from .views import BookmarkDetail, BookmarkListCreate

urlpatterns = [
    path('', BookmarkListCreate.as_view(), name='bookmark-list-create'),
    path('<int:pk>/', BookmarkDetail.as_view(), name='bookmark-detail'),
]
