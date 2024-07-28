from rest_framework import generics
from .models import Like
from .serializers import LikeSerializer
from api_blog.permissions import IsOwnerOrReadOnly


class LikeListCreateView(generics.ListCreateAPIView):
    """
    View for listing and creating likes.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    View for retrieving and deleting a like.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
