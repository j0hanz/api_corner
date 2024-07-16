from django.contrib import admin
from .models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'comment', 'created_at')
    list_filter = ('user', 'post', 'comment', 'created_at')
    search_fields = ('user__username', 'post__content', 'comment__content')
    ordering = ['-created_at']
