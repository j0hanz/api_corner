from rest_framework import generics, permissions
from .models import Bookmark
from .serializers import BookmarkSerializer
from api_blog.permissions import IsOwnerOrReadOnly


class BookmarkListCreateView(generics.ListCreateAPIView):
    """
    View for listing and creating bookmarks.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Bookmark.objects.all().order_by('-created_at')
    serializer_class = BookmarkSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookmarkRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    """
    View for retrieving and deleting a bookmark.
    """

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
