from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import News
from .serializers import NewsSerializer
from api_blog.permissions import IsAuthorOrReadOnly


class NewsListCreateView(generics.ListCreateAPIView):
    """
    View for listing and creating news articles.
    """

    permission_classes = [IsAuthorOrReadOnly]
    queryset = News.objects.all().order_by('-published_at')
    serializer_class = NewsSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = ['category', 'author__username']
    search_fields = ['title', 'content', 'category']
    ordering_fields = ['published_at', 'updated_at', 'title']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class NewsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting a single news article.
    Only the author can update or delete the article.
    """

    permission_classes = [
        IsAuthorOrReadOnly,
    ]
    queryset = News.objects.all()
    serializer_class = NewsSerializer
