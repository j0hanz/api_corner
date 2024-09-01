from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from api_blog.permissions import IsOwnerOrReadOnly

from .models import Comment
from .serializers import CommentDetailSerializer, CommentSerializer


class CommentListCreateView(generics.ListCreateAPIView):
    """View for listing and creating comments."""

    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.annotate(likes_count=Count('likes')).order_by(
        '-created_at'
    )
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting a single comment.
    Only the owner can update or delete the comment.
    """

    serializer_class = CommentDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
