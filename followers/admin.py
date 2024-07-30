from django.contrib import admin
from .models import Follower


@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ('owner', 'followed_user', 'created_at')
    search_fields = ['owner__username', 'followed_user__username']
    ordering = ('-created_at',)
    list_filter = ('owner', 'followed_user', 'created_at')
