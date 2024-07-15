from rest_framework import generics, permissions, filters, serializers
from django_filters.rest_framework import DjangoFilterBackend
from .models import Report
from .serializers import ReportSerializer


class ReportListCreateView(generics.ListCreateAPIView):
    """
    View for listing and creating reports.
    """

    permission_classes = [permissions.IsAuthenticated]
    queryset = Report.objects.all().order_by('-reported_at')
    serializer_class = ReportSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = ['post', 'comment', 'user']
    search_fields = [
        'user__username',
        'post__title',
        'comment__content',
        'reason',
    ]
    ordering_fields = ['reported_at', 'user', 'post', 'comment']

    def perform_create(self, serializer):
        post = self.request.data.get('post')
        comment = self.request.data.get('comment')
        if not post and not comment:
            raise serializers.ValidationError(
                {"post": "Either post or comment must be provided."}
            )
        serializer.save(user=self.request.user)
