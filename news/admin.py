from django.contrib import admin

from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """Admin configuration for the News model."""

    list_display = (
        'id',
        'title',
        'author',
        'category',
        'published_at',
        'updated_at',
        'image',
    )
    list_filter = ('category', 'author', 'published_at')
    search_fields = (
        'title',
        'content',
        'author__username',
        'category',
        'image',
    )
    ordering = ['-published_at']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('author')
