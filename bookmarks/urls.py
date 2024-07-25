from django.urls import path
from .views import BookmarkListCreate, BookmarkDetail

urlpatterns = [
    path('', BookmarkListCreate.as_view(), name='bookmark-list-create'),
    path('<int:pk>/', BookmarkDetail.as_view(), name='bookmark-detail'),
]
