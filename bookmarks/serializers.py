from rest_framework import serializers
from .models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    """
    Serializer for the Bookmark model.
    Includes logic to prevent duplicate bookmarks.
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    post_content = serializers.CharField(source='post.content', read_only=True)
    post_owner = serializers.CharField(
        source='post.owner.username', read_only=True
    )

    def create(self, validated_data):
        """
        Creates a Bookmark instance.
        Checks if the user already bookmarked the post.
        Throws an error if the user already bookmarked that instance.
        """
        owner = self.context['request'].user
        post = validated_data.get('post')

        if Bookmark.objects.filter(owner=owner, post=post).exists():
            raise serializers.ValidationError(
                'You have already bookmarked this post.'
            )

        return super().create(validated_data)

    class Meta:
        model = Bookmark
        fields = [
            'id',
            'owner',
            'post',
            'post_content',
            'post_owner',
            'created_at',
        ]
