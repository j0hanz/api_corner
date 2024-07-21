from rest_framework import serializers
from .models import Profile
from pathlib import Path


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def update(self, instance, validated_data):
        image = validated_data.get('image', None)
        if image and instance.image:
            destroy(instance.image.public_id)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def validate_image(self, value):
        path = Path(value.name)
        file_extension = path.suffix.lower()
        valid_extensions = ['.jpg', '.jpeg', '.png']
        if file_extension not in valid_extensions:
            raise serializers.ValidationError(
                'Image must be jpg, jpeg, or png!'
            )
        return value

    class Meta:
        model = Profile
        fields = [
            'owner',
            'first_name',
            'last_name',
            'bio',
            'image',
            'location',
            'url_link',
            'contact_email',
            'is_active',
            'created_at',
            'updated_at',
            'is_owner',
            'posts_count',
            'followers_count',
            'following_count',
        ]
        read_only_fields = ['owner', 'created_at', 'updated_at']
