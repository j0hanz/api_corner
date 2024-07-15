from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Register Comment model in the admin panel.
    """

    list_display = (
        'id',
        'user',
        'post',
        'content',
        'created_at',
        'updated_at',
    )
    list_filter = ('user', 'post', 'created_at')
    search_fields = ('user__username', 'post__title', 'content')
    ordering = ['-created_at']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('user', 'post')
        return queryset
