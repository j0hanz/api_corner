from rest_framework import serializers
from .models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    """
    Serializer for the Bookmark model.
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    created_at = serializers.DateTimeField(format='%d %b %Y', read_only=True)

    class Meta:
        model = Bookmark
        fields = ['id', 'owner', 'post', 'created_at']

    def validate(self, data):
        owner = self.context['request'].user
        post = data.get('post')
        if Bookmark.objects.filter(owner=owner, post=post).exists():
            raise serializers.ValidationError(
                'You already bookmarked this post'
            )
        return data

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)
