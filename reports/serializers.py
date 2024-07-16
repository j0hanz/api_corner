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
    reported_user_username = serializers.ReadOnlyField(
        source='reported_user.username'
    )

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
            'reported_user',
            'reported_user_username',
            'user',
            'reason',
            'reported_at',
        ]

    def validate(self, data):
        if not any(
            data.get(field) for field in ['post', 'comment', 'reported_user']
        ):
            raise serializers.ValidationError(
                "Either post, comment, or reported_user must be provided."
            )
        return data
