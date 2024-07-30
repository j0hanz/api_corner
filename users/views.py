from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count, F
from .models import Profile
from .serializers import ProfileSerializer
from api_blog.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    serializer_class = ProfileSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile',
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followers__created_at',
    ]

    def get_queryset(self):
        return (
            Profile.objects.select_related('owner')
            .annotate(
                posts_count=Count('owner__posts', distinct=True),
                followers_count=Count('owner__followers', distinct=True),
                following_count=Count('owner__following', distinct=True),
            )
            .order_by(
                F('followers_count').desc(nulls_last=True), '-created_at'
            )
        )


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return (
            Profile.objects.select_related('owner')
            .annotate(
                posts_count=Count('owner__posts', distinct=True),
                followers_count=Count('owner__followers', distinct=True),
                following_count=Count('owner__following', distinct=True),
            )
            .order_by('-created_at')
        )
