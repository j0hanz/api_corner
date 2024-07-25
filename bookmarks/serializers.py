from rest_framework import serializers
from .models import Bookmark
from posts.models import Post


class BookmarkSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    post_content = serializers.CharField(source='post.content', read_only=True)
    post_image = serializers.ImageField(source='post.image', read_only=True)
    post_owner = serializers.CharField(
        source='post.owner.username', read_only=True
    )

    class Meta:
        model = Bookmark
        fields = [
            'id',
            'owner',
            'post',
            'post_content',
            'post_image',
            'post_owner',
            'created_at',
        ]
