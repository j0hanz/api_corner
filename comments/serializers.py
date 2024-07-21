from rest_framework import serializers
from .models import Comment
import datetime
from likes.models import Like


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
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
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
            'like_id',
            'likes_count',
        ]

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        """
        Gets the like id if the user has liked the comment.
        If user is not authenticated, or has not liked the comment,
        return None.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, comment=obj).first()
            return like.id if like else None
        return None

    def get_likes_count(self, obj):
        """
        Returns the number of likes for the comment.
        "likes" is referencing the Like model, connected to the Comment model,
        through related_name="likes".
        """
        return obj.likes.count()

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
