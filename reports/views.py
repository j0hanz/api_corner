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
    filterset_fields = ['post', 'user']
    search_fields = ['user__username', 'post__title', 'reason']
    ordering_fields = ['reported_at', 'user', 'post']

    def perform_create(self, serializer):
        post = self.request.data.get('post')
        if not post:
            raise serializers.ValidationError(
                {"post": "This field is required."}
            )
        serializer.save(user=self.request.user)
