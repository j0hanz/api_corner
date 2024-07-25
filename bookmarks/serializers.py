from rest_framework import serializers
from .models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    post_content = serializers.ReadOnlyField(source='post.content')
    post_owner = serializers.ReadOnlyField(source='post.owner.username')
    created_at = serializers.DateTimeField(format='%d %b %Y', read_only=True)

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

    def validate(self, data):
        owner = self.context['request'].user
        post = data.get('post')
        if Bookmark.objects.filter(owner=owner, post=post).exists():
            existing_bookmark = Bookmark.objects.get(owner=owner, post=post)
            data['existing_bookmark'] = existing_bookmark
        return data

    def create(self, validated_data):
        if 'existing_bookmark' in validated_data:
            return validated_data['existing_bookmark']
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)
