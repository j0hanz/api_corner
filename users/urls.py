from django.urls import path
from .views import (
    ProfileList,
    ProfileDetail,
    FavoriteMovieGenreList,
    FavoriteMusicGenreList,
    FavoriteSportList,
)

urlpatterns = [
    path('', ProfileList.as_view(), name='profile-list'),
    path('<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    path(
        'favorite-movie-genres/',
        FavoriteMovieGenreList.as_view(),
        name='favorite-movie-genres',
    ),
    path(
        'favorite-music-genres/',
        FavoriteMusicGenreList.as_view(),
        name='favorite-music-genres',
    ),
    path(
        'favorite-sports/', FavoriteSportList.as_view(), name='favorite-sports'
    ),
]
