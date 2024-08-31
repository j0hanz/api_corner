from django.contrib import admin

from .models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['owner', 'post', 'comment', 'created_at']
    list_filter = ['created_at']
    search_fields = ['owner__username', 'post__title', 'comment__content']
