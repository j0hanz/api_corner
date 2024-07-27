from rest_framework import generics, filters, serializers
from django_filters.rest_framework import DjangoFilterBackend
from .models import Report
from .serializers import ReportSerializer
from api_blog.permissions import IsOwnerOrReadOnly


class ReportListCreateView(generics.ListCreateAPIView):
    """
    View for listing and creating reports.
    """

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Report.objects.all().order_by('-reported_at')
    serializer_class = ReportSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = ['post', 'comment', 'reported_user', 'owner']
    search_fields = [
        'owner__username',
        'post__content',
        'comment__content',
        'reported_user__username',
        'reason',
    ]
    ordering_fields = [
        'reported_at',
        'owner',
        'post',
        'comment',
        'reported_user',
    ]

    def perform_create(self, serializer):
        if (
            not self.request.data.get('post')
            and not self.request.data.get('comment')
            and not self.request.data.get('reported_user')
        ):
            raise serializers.ValidationError(
                {
                    "post": "Either post, comment, or reported_user must be provided."
                }
            )
        serializer.save(owner=self.request.user)
