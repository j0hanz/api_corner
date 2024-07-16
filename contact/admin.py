from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Register Contact model in the admin panel.
    """

    list_display = ('id', 'user', 'email', 'category', 'subject', 'created_at')
    list_filter = ('user', 'category', 'created_at')
    search_fields = (
        'user__username',
        'email',
        'category',
        'subject',
        'message',
    )
    ordering = ['-created_at']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('user')
