from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, serializers

from api_blog.permissions import IsOwnerOrReadOnly

from .models import Post, Report
from .serializers import ReportSerializer


class ReportListCreateView(generics.ListCreateAPIView):
    """View for listing and creating reports."""

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
        post_id = self.request.data.get('post')
        comment_id = self.request.data.get('comment')

        if not post_id and not comment_id:
            raise serializers.ValidationError(
                'Either post or comment must be provided.'
            )

        if post_id:
            try:
                post_instance = Post.objects.get(id=post_id)
                reported_user = post_instance.owner
            except Post.DoesNotExist:
                raise serializers.ValidationError(
                    'The provided post does not exist.'
                )
        else:
            reported_user = None

        serializer.save(owner=self.request.user, reported_user=reported_user)
