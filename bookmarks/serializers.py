from rest_framework import serializers
from .models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    """
    Serializer for the Bookmark model.
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    post_content = serializers.ReadOnlyField(source='post.content')
    post_owner = serializers.ReadOnlyField(source='post.owner.username')
    post_owner_profile_image = serializers.ReadOnlyField(
        source='post.owner.profile.image.url'
    )
    post_owner_profile_id = serializers.ReadOnlyField(
        source='post.owner.profile.id'
    )
    created_at = serializers.DateTimeField(format='%d %b %Y', read_only=True)

    class Meta:
        model = Bookmark
        fields = [
            'id',
            'owner',
            'post',
            'post_content',
            'post_owner',
            'post_owner_profile_image',
            'post_owner_profile_id',
            'created_at',
        ]

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        try:
            return super().create(validated_data)
        except:
            return Bookmark.objects.get(
                owner=validated_data['owner'], post=validated_data['post']
            )
