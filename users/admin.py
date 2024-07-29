from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'owner',
        'first_name',
        'last_name',
        'is_active',
        'created_at',
        'updated_at',
    ]
    list_editable = [
        'is_active',
    ]
