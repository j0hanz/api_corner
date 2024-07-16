from django.contrib import admin
from .models import Bookmark


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'post', 'created_at')
    list_filter = ('owner', 'post', 'created_at')
    search_fields = ('owner__username', 'post__content')
    ordering = ['-created_at']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('owner', 'post')
