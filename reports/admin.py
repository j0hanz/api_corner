from django.contrib import admin
from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    """
    Register Report model in the admin panel.
    """

    list_display = ('id', 'user', 'post', 'comment', 'reason', 'reported_at')
    list_filter = ('user', 'post', 'comment', 'reported_at')
    search_fields = (
        'user__username',
        'post__title',
        'comment__content',
        'reason',
    )
    ordering = ['-reported_at']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('user', 'post', 'comment')
        return queryset
