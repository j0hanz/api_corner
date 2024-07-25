from rest_framework import generics
from .models import Follower
from .serializers import FollowerSerializer
from api_blog.permissions import IsOwnerOrReadOnly


class FollowerListCreateView(generics.ListCreateAPIView):
    """
    View for listing and creating follower relationships.
    """

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all().order_by('-created_at')
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user)


class FollowerRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    """
    View for retrieving and deleting a follower relationship.
    """

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
