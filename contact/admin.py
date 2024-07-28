from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for the Contact model.
    """

    list_display = (
        'id',
        'owner',
        'email',
        'category',
        'subject',
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
    ordering = ['-created_at']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('owner')
