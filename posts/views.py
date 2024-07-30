from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
from .models import Post
from .serializers import PostSerializer
from api_blog.permissions import IsOwnerOrReadOnly


class PostQuerySet(generics.GenericAPIView):
    """
    Base queryset for post views.
    """

    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comments', distinct=True),
    ).order_by('-created_at')


class PostListCreateView(PostQuerySet, generics.ListCreateAPIView):
    """
    List and create posts. Only authenticated users can create posts.
    """

    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'owner__profile',
        'likes__owner__profile',
        'tags__name',
        'content',
    ]
    search_fields = ['owner__username', 'content', 'tags__name']
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetailView(PostQuerySet, generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, and delete a single post. Only the owner can modify it.
    """

    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comments', distinct=True),
    ).order_by('-created_at')
