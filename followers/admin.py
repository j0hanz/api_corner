from django.contrib import admin
from .models import Follower


@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ('owner', 'followed', 'created_at')
    search_fields = ['owner__username', 'followed__username']
    ordering = ('-created_at',)
    list_filter = ('owner', 'followed', 'created_at')
