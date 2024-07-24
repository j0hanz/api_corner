from django.contrib import admin
from django.utils import timezone
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Admin configuration for the Profile model."""

    list_display = (
        'id',
        'owner',
        'first_name',
        'last_name',
        'is_active',
        'created_at',
        'updated_at',
        'owner_email',
    )
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = (
        'owner__username',
        'first_name',
        'last_name',
        'owner__email',
    )
    ordering = ['-created_at']
    autocomplete_fields = ['owner']
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (
            None,
            {'fields': ('owner', 'first_name', 'last_name', 'bio', 'image')},
        ),
        (
            'Contact Info',
            {'fields': ('location', 'url_link', 'contact_email')},
        ),
        ('Status', {'fields': ('is_active',)}),
        ('Dates', {'fields': ('created_at', 'updated_at')}),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('owner')

    def owner_email(self, obj):
        return obj.owner.email if obj.owner else None

    owner_email.short_description = 'Owner Email'

    def save_model(self, request, obj, form, change):
        if change:
            obj.updated_at = timezone.now()
        super().save_model(request, obj, form, change)
