from rest_framework import generics, status
from rest_framework.response import Response
from .models import Bookmark
from .serializers import BookmarkSerializer
from api_blog.permissions import IsOwnerOrReadOnly


class BookmarkListCreateView(generics.ListCreateAPIView):
    """
    List and create bookmarks.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BookmarkSerializer

    def get_queryset(self):
        """
        Return bookmarks for the authenticated user.
        """
        user = self.request.user
        if user.is_authenticated:
            return Bookmark.objects.filter(owner=user).order_by('-created_at')
        return Bookmark.objects.none()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookmarkRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    """
    Retrieve and delete a bookmark.
    """

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
