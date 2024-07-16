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
    filterset_fields = ['post', 'comment', 'reported_user', 'user']
    search_fields = [
        'user__username',
        'comment__content',
        'reported_user__username',
        'reason',
    ]
    ordering_fields = [
        'reported_at',
        'user',
        'post',
        'comment',
        'reported_user',
    ]

    def perform_create(self, serializer):
        data = self.request.data
        if not any(
            data.get(field) for field in ['post', 'comment', 'reported_user']
        ):
            raise serializers.ValidationError(
                {
                    "non_field_errors": "Either post, comment, or reported_user must be provided."
                }
            )
        serializer.save(user=self.request.user)
