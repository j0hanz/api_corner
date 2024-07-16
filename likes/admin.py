from django.contrib import admin
from .models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    """
    Register Like model in the admin panel.
    """

    list_display = ('id', 'owner', 'post', 'comment', 'created_at')
    list_filter = ('owner', 'post', 'comment', 'created_at')
    search_fields = ('owner__username', 'post__content', 'comment__content')
    ordering = ['-created_at']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('owner', 'post', 'comment')
