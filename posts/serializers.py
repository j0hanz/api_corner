from rest_framework import serializers
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
    likes_count = serializers.SerializerMethodField()
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
        """
        Check if the request user is the owner of the post.
        """
        request = self.context.get('request')
        return request.user == obj.owner if request else False

    def get_created_at(self, obj):
        """
        Return a human-readable string representing the creation time.
        """
        return shortnaturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """
        Return a human-readable string representing the last update time.
        """
        return shortnaturaltime(obj.updated_at)

    def get_like_id(self, obj):
        """
        Get the like id if the user has liked the post.
        Return None if the user is not authenticated or has not liked the post.
        """
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            like = Like.objects.filter(owner=request.user, post=obj).first()
            return like.id if like else None
        return None

    def get_likes_count(self, obj):
        """
        Return the number of likes for the post.
        """
        return obj.likes.count()

    def get_comments_count(self, obj):
        """
        Return the number of comments for the post.
        """
        return obj.comments.count()

    def validate_image(self, value):
        """
        Validate the uploaded image.
        """
        self._validate_file_size(value)
        self._validate_image_dimensions(value)
        return value

    def _validate_file_size(self, value):
        """
        Validate the file size of the uploaded image.
        """
        max_size = 5 * 1024 * 1024
        if value.size > max_size:
            raise serializers.ValidationError('Image size larger than 5MB!')

    def _validate_image_dimensions(self, value):
        """
        Validate the dimensions of the uploaded image.
        """
        max_dimension = 4096
        if (
            value.image.height > max_dimension
            or value.image.width > max_dimension
        ):
            raise serializers.ValidationError(
                'Image dimensions larger than 4096px!'
            )

    def validate_content(self, value):
        """
        Validate the content of the post.
        """
        if not value.strip():
            raise serializers.ValidationError("Post content cannot be empty.")
        return value
