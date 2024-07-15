from rest_framework import serializers
from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    """
    Serializer for the Report model.
    """

    user = serializers.ReadOnlyField(source='user.username')
    post_id = serializers.ReadOnlyField(source='post.id')
    post_title = serializers.ReadOnlyField(source='post.title')
    comment_id = serializers.ReadOnlyField(source='comment.id')
    comment_content = serializers.ReadOnlyField(source='comment.content')

    class Meta:
        model = Report
        fields = [
            'id',
            'post',
            'post_id',
            'post_title',
            'comment',
            'comment_id',
            'comment_content',
            'user',
            'reason',
            'reported_at',
        ]

    def validate(self, data):
        if not data.get('post') and not data.get('comment'):
            raise serializers.ValidationError(
                "Either post or comment must be provided."
            )
        return data
