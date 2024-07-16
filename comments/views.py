from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer
from api_blog.permissions import IsOwnerOrReadOnly


class CommentListCreateView(generics.ListCreateAPIView):
    """
    View for listing and creating comments.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = ['post', 'owner']
    search_fields = ['owner__username', 'post__content', 'content']
    ordering_fields = ['created_at', 'owner', 'post']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting a single comment.
    Only the owner can update or delete the comment.
    """

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
