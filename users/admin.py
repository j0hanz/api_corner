from django.contrib import admin
from .models import (
    Profile,
    FavoriteMovieGenre,
    FavoriteMusicGenre,
    FavoriteSport,
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Profile model.
    """

    list_display = (
        'id',
        'owner',
        'first_name',
        'last_name',
        'favorite_movie_genre',
        'favorite_music_genre',
        'favorite_sport',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_active',
        'created_at',
        'updated_at',
        'favorite_movie_genre',
        'favorite_music_genre',
        'favorite_sport',
    )
    search_fields = (
        'owner__username',
        'first_name',
        'last_name',
        'favorite_movie_genre__genre',
        'favorite_music_genre__genre',
        'favorite_sport__sport',
    )
    ordering = ['-created_at']
    autocomplete_fields = [
        'favorite_movie_genre',
        'favorite_music_genre',
        'favorite_sport',
    ]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related(
            'owner',
            'favorite_movie_genre',
            'favorite_music_genre',
            'favorite_sport',
        )


@admin.register(FavoriteMovieGenre)
class FavoriteMovieGenreAdmin(admin.ModelAdmin):
    """
    Admin configuration for the FavoriteMovieGenre model.
    """

    list_display = ('id', 'genre')
    search_fields = ('genre',)
    ordering = ['genre']


@admin.register(FavoriteMusicGenre)
class FavoriteMusicGenreAdmin(admin.ModelAdmin):
    """
    Admin configuration for the FavoriteMusicGenre model.
    """

    list_display = ('id', 'genre')
    search_fields = ('genre',)
    ordering = ['genre']


@admin.register(FavoriteSport)
class FavoriteSportAdmin(admin.ModelAdmin):
    """
    Admin configuration for the FavoriteSport model.
    """

    list_display = ('id', 'sport')
    search_fields = ('sport',)
    ordering = ['sport']
