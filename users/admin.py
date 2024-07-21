from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Profile model.
    """

    list_display = (
        'id',
        'owner',
        'first_name',
        'last_name',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_active',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'owner__username',
        'first_name',
        'last_name',
    )
    ordering = ['-created_at']
    autocomplete_fields = []

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related(
            'owner',
        )
