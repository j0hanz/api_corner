from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Admin panel configuration for the Contact model."""

    fields = (
        'owner',
        'email',
        'category',
        'subject',
        'message',
    )
    list_display = (
        'id',
        'owner',
        'email',
        'category',
        'subject',
        'message',
        'created_at',
    )
    list_filter = ('owner', 'category', 'created_at')
    search_fields = (
        'owner__username',
        'email',
        'category',
        'subject',
        'message',
    )
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('owner')
