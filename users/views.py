from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
from .models import (
    Profile,
    FavoriteMovieGenre,
    FavoriteMusicGenre,
    FavoriteSport,
)
from .serializers import (
    ProfileSerializer,
    FavoriteMovieGenreSerializer,
    FavoriteMusicGenreSerializer,
    FavoriteSportSerializer,
)
from api_blog.permissions import IsOwnerOrReadOnly


class FavoriteMovieGenreList(generics.ListAPIView):
    queryset = FavoriteMovieGenre.objects.all()
    serializer_class = FavoriteMovieGenreSerializer


class FavoriteMusicGenreList(generics.ListAPIView):
    queryset = FavoriteMusicGenre.objects.all()
    serializer_class = FavoriteMusicGenreSerializer


class FavoriteSportList(generics.ListAPIView):
    queryset = FavoriteSport.objects.all()
    serializer_class = FavoriteSportSerializer


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__posts', distinct=True),
        followers_count=Count('owner__followers', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = [
        'owner__following__followed',
        'owner__followers__follower',
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followers__created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__posts', distinct=True),
        followers_count=Count('owner__followers', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
