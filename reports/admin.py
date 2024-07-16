from django.contrib import admin
from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    """
    Register Report model in the admin panel.
    """

    list_display = (
        'id',
        'owner',
        'post',
        'comment',
        'reported_user',
        'reason',
        'reported_at',
    )
    list_filter = ('owner', 'post', 'comment', 'reported_user', 'reported_at')
    search_fields = (
        'owner__username',
        'post__content',
        'comment__content',
        'reported_user__username',
        'reason',
    )
    ordering = ['-reported_at']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related(
            'owner', 'post', 'comment', 'reported_user'
        )
