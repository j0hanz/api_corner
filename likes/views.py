from rest_framework import generics, permissions
from .models import Like
from .serializers import LikeSerializer
from api_blog.permissions import IsOwnerOrReadOnly


class LikeListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Like.objects.all().order_by('-created_at')
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
