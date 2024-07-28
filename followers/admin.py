from django.contrib import admin
from .models import Follower


@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Follower model.
    """

    fields = ('follower', 'followed', 'created_at')
    list_display = ('id', 'follower', 'followed', 'created_at')
    list_filter = ('follower', 'followed', 'created_at')
    search_fields = ('follower__username', 'followed__username')
    ordering = ('-created_at',)

    def get_queryset(self, request):
        return (
            super()
            .get_queryset(request)
            .select_related('follower', 'followed')
        )
