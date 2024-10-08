from datetime import UTC, datetime, timedelta

from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from bookmarks.models import Bookmark
from likes.models import Like

from .models import Post


def shortnaturaltime(value):
    """Return a human-readable string representing the time delta from now to the given value."""
    now = datetime.now(UTC)
    delta = now - value

    if delta < timedelta(minutes=1):
        return 'just now'
    if delta < timedelta(hours=1):
        return f'{int(delta.total_seconds() // 60)}m'
    if delta < timedelta(days=1):
        return f'{int(delta.total_seconds() // 3600)}h'
    return f'{delta.days}d'


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    """Serializer for the Post model."""

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    tags = TagListSerializerField()
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    bookmark_id = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    filtered_image_url = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """Check if the request user is the owner of the post."""
        request = self.context.get('request')
        return request and request.user == obj.owner

    def get_created_at(self, obj):
        """Return a human-readable string representing the creation time."""
        return shortnaturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """Return a human-readable string representing the last update time."""
        return shortnaturaltime(obj.updated_at)

    def get_like_id(self, obj):
        """Get the like id if the user has liked the post.
        Return None if the user is not authenticated or has not liked the post.
        """
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            like = Like.objects.filter(owner=request.user, post=obj).first()
            return like.id if like else None
        return None

    def get_bookmark_id(self, obj):
        """Get the bookmark id if the user has bookmarked the post.
        Return None if the user is not authenticated or has not bookmarked the post.
        """
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            bookmark = Bookmark.objects.filter(
                owner=request.user, post=obj
            ).first()
            return bookmark.id if bookmark else None
        return None

    def get_likes_count(self, obj):
        """Return the number of likes for the post."""
        return obj.likes.count()

    def get_comments_count(self, obj):
        """Return the number of comments for the post."""
        return obj.comments.count()

    def get_filtered_image_url(self, obj):
        """Return the URL of the image with the applied filter using Cloudinary transformations."""
        if obj.image:
            transformations = {
                'GRAYSCALE': 'e_grayscale',
                'SEPIA': 'e_sepia',
                'NEGATIVE': 'e_negate',
                'BRIGHTNESS': 'e_brightness:30',
                'CONTRAST': 'e_contrast:30',
                'SATURATION': 'e_saturation:30',
                'HUE_ROTATE': 'e_hue:90',
                'BLUR': 'e_blur:200',
                'SHARPEN': 'e_sharpen',
                'VINTAGE': 'e_vintage',
                'VIGNETTE': 'e_vignette:20',
                'CROSS_PROCESS': 'e_cross_process',
                'HDR': 'e_hdr',
                'EDGE_DETECT': 'e_edge_detect',
                'EMBOSS': 'e_emboss',
                'SOLARIZE': 'e_solarize',
                'POSTERIZE': 'e_posterize',
                'PIXELATE': 'e_pixelate',
                'CARTOON': 'e_cartoon',
                'DUOTONE': 'e_duotone',
            }
            transformation = transformations.get(obj.image_filter, '')
            return (
                f'{obj.image.url}?transformation={transformation}'
                if transformation
                else obj.image.url
            )
        return ''

    def validate(self, data):
        """Validate that either content or image is present."""
        request = self.context.get('request')
        if request and request.method in ['PUT', 'PATCH']:
            instance = self.instance
            if (
                not data.get('content')
                and not data.get('image')
                and not instance.image
            ):
                raise serializers.ValidationError(
                    'You must upload an image or write some content.'
                )
        else:
            if not data.get('content') and not data.get('image'):
                raise serializers.ValidationError(
                    'You must upload an image or write some content.'
                )
        return data

    def update(self, instance, validated_data):
        """Handle updating the Post, ensuring the image is retained if not modified."""
        if not validated_data.get('image') and instance.image:
            validated_data['image'] = instance.image
        return super().update(instance, validated_data)

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
            'bookmark_id',
            'filtered_image_url',
        ]
