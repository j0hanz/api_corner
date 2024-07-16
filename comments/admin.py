from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Register Comment model in the admin panel.
    """

    list_display = (
        'id',
        'owner',
        'post',
        'content',
        'created_at',
        'updated_at',
    )
    list_filter = ('owner', 'post', 'created_at')
    search_fields = ('owner__username', 'post__content', 'content')
    ordering = ['-created_at']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('owner', 'post')
