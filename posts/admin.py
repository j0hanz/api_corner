from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Post model.
    """

    list_display = ('id', 'owner', 'content', 'created_at', 'updated_at')
    list_filter = ('owner', 'created_at', 'updated_at')
    search_fields = ('owner__username', 'content', 'tags__name')
    ordering = ['-created_at']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('owner').prefetch_related('tags')
