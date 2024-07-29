from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
from .models import Profile
from .serializers import ProfileSerializer
from api_blog.permissions import IsOwnerOrReadOnly


class ProfileQuerySet(generics.ListAPIView):
    """
    Base queryset for listing and detailing profiles.
    """

    queryset = Profile.objects.annotate(
        posts_count=Count('owner__posts', distinct=True),
        followers_count=Count('owner__followers', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_at')


class ProfileList(ProfileQuerySet):
    """
    View for listing profiles.
    """

    serializer_class = ProfileSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followers__created_at',
    ]

    def get_queryset(self):
        queryset = super().get_queryset()

        followed_by = self.request.query_params.get('followed_by')
        followed = self.request.query_params.get('followed')

        if followed_by:
            queryset = queryset.filter(owner__followers__owner__id=followed_by)
        if followed:
            queryset = queryset.filter(owner__following__owner__id=followed)

        return queryset


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView, ProfileQuerySet):
    """
    View for retrieving, updating, and deleting profiles.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
