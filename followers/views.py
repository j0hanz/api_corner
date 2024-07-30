from rest_framework import generics
from api_blog.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


class FollowerList(generics.ListCreateAPIView):
    """
    List all followers for the currently authenticated user or create a new follower relationship.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FollowerSerializer

    def get_queryset(self):
        return Follower.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve or delete a follower relationship.
    """

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
