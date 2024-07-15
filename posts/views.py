from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post
from .serializers import PostSerializer
from api_blog.permissions import IsOwnerOrReadOnly


class PostListCreateView(generics.ListCreateAPIView):
    """
    View for listing and creating posts.
    A post can be created by an authenticated user.
    """

    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all().order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__profile',
        'owner__profile__id',
    ]
    search_fields = [
        'owner__username',
        'title',
        'tags__name',
    ]
    ordering_fields = [
        'created_at',
    ]

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if 'favorites' in self.request.query_params and user.is_authenticated:
            queryset = queryset.filter(favorites__owner=user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting a single post.
    Only the owner can update or delete the post.
    """

    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all().order_by('-created_at')
