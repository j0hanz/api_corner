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
        user = self.request.user
        return (
            Bookmark.objects.filter(owner=user).order_by('-created_at')
            if user.is_authenticated
            else Bookmark.objects.none()
        )


class BookmarkDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve and delete a bookmark.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BookmarkSerializer

    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)
