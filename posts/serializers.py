from rest_framework import serializers
from pathlib import Path
from taggit.serializers import TagListSerializerField, TaggitSerializer
from .models import Post
from likes.models import Like
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


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    tags = TagListSerializerField()
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'content',
            'image',
            'image_filter',
            'tags',
            'created_at',
            'updated_at',
            'like_id',
            'likes_count',
            'comments_count',
        ]

    def get_is_owner(self, obj):
        request = self.context.get('request', None)
        return request.user == obj.owner if request else False

    def get_created_at(self, obj):
        return shortnaturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return shortnaturaltime(obj.updated_at)

    def get_like_id(self, obj):
        """
        Gets the like id if the user has liked the post.
        If user is not authenticated, or has not liked the post,
        return None.
        """
        user = self.context.get('request').user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, post=obj).first()
            return like.id if like else None
        return None

    def get_likes_count(self, obj):
        """
        Returns the number of likes for the post.
        "likes" is referencing the Like model, connected to the Post model,
        through related_name="likes".
        """
        return obj.likes.count()

    def get_comments_count(self, obj):
        """
        Returns the number of comments for the post.
        "comments" is referencing the Comment model,
        connected to the Post model,
        through related_name="comments".
        """
        return obj.comments.count()

    def validate_image(self, value):
        self._validate_file_extension(value)
        self._validate_file_size(value)
        self._validate_image_dimensions(value)
        return value

    def _validate_file_extension(self, value):
        file_extension = Path(value.name).suffix.lower()
        valid_extensions = {'.jpg', '.jpeg', '.png'}
        if file_extension not in valid_extensions:
            raise serializers.ValidationError(
                'Image must be jpg, jpeg, or png!'
            )

    def _validate_file_size(self, value):
        max_size = 5 * 1024 * 1024
        if value.size > max_size:
            raise serializers.ValidationError('Image size larger than 5MB!')

    def _validate_image_dimensions(self, value):
        max_dimension = 4096
        if (
            value.image.height > max_dimension
            or value.image.width > max_dimension
        ):
            raise serializers.ValidationError(
                'Image dimensions larger than 4096px!'
            )

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Post content cannot be empty.")
        return value
