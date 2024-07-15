from rest_framework import serializers
from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    """
    Serializer for the Report model.
    """

    user = serializers.ReadOnlyField(source='user.username')
    post_id = serializers.ReadOnlyField(source='post.id')
    post_title = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Report
        fields = [
            'id',
            'post',
            'post_id',
            'post_title',
            'user',
            'reason',
            'reported_at',
        ]
