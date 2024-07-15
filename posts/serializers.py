from rest_framework import serializers
from pathlib import Path
from taggit.serializers import TagListSerializerField, TaggitSerializer
from .models import Post


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    tags = TagListSerializerField()

    class Meta:
        model = Post
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'title',
            'content',
            'excerpt',
            'image',
            'image_filter',
            'tags',
            'created_at',
            'updated_at',
        ]

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def validate_image(self, value):
        self._validate_file_extension(value)
        self._validate_file_size(value)
        self._validate_image_dimensions(value)
        return value

    def _validate_file_extension(self, value):
        path = Path(value.name)
        file_extension = path.suffix.lower()
        valid_extensions = ['.jpg', '.jpeg', '.png']
        if file_extension not in valid_extensions:
            raise serializers.ValidationError(
                'Image must be jpg, jpeg or png!'
            )

    def _validate_file_size(self, value):
        if value.size > 5 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 5MB!')

    def _validate_image_dimensions(self, value):
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Post content cannot be empty.")
        return value
