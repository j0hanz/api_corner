from rest_framework import serializers
from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    """
    Serializer for the Report model.
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    post_id = serializers.ReadOnlyField(source='post.id')
    post_content = serializers.ReadOnlyField(source='post.content')
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
            'post_content',
            'comment',
            'comment_id',
            'comment_content',
            'reported_user',
            'reported_user_username',
            'owner',
            'reason',
            'reported_at',
        ]

    def validate(self, data):
        if (
            not data.get('post')
            and not data.get('comment')
            and not data.get('reported_user')
        ):
            raise serializers.ValidationError(
                "Either post, comment, or reported_user must be provided."
            )
        return data
