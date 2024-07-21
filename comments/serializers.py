from rest_framework import serializers
from pathlib import Path
from .models import Comment
import datetime


def shortnaturaltime(value):
    now = datetime.datetime.now(datetime.timezone.utc)
    delta = now - value

    if delta < datetime.timedelta(minutes=1):
        return 'just now'
    elif delta < datetime.timedelta(hours=1):
        return f'{int(delta.total_seconds() // 60)}m'
    elif delta < datetime.timedelta(days=1):
        return f'{int(delta.total_seconds() // 3600)}h'
    else:
        return f'{delta.days}d'


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model.
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'owner',
            'post',
            'content',
            'created_at',
            'updated_at',
            'is_owner',
            'profile_id',
            'profile_image',
        ]

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return shortnaturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return shortnaturaltime(obj.updated_at)


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for detailed view of the Comment model.
    Ensures the post is read-only.
    """

    post = serializers.ReadOnlyField(source='post.id')
