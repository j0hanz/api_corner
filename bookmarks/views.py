from rest_framework import generics
from .models import Bookmark
from .serializers import BookmarkSerializer
from api_blog.permissions import IsOwnerOrReadOnly


class BookmarkListCreate(generics.ListCreateAPIView):
    """
    List and create bookmarks.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BookmarkSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Bookmark.objects.filter(owner=self.request.user).order_by(
                '-created_at'
            )
        return Bookmark.objects.none()


class BookmarkDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve and delete a bookmark.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BookmarkSerializer

    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)
