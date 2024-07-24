from rest_framework import serializers
from .models import Profile
from pathlib import Path
from cloudinary.uploader import destroy
import logging

logger = logging.getLogger(__name__)


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

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

    def get_is_owner(self, obj):
        """
        Check if the request user is the owner of the profile.
        """
        request = self.context.get('request')
        return request and request.user == obj.owner

    def update(self, instance, validated_data):
        """
        Update profile and handle image replacement in Cloudinary.
        """
        new_image = validated_data.get('image')
        if (
            new_image
            and instance.image
            and hasattr(instance.image, 'public_id')
        ):
            try:
                destroy(instance.image.public_id)
            except Exception as e:
                logger.error(f"Error destroying old image: {e}")

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def validate_image(self, value):
        """
        Validate the image field to ensure it has a valid extension.
        """
        valid_extensions = {'.jpg', '.jpeg', '.png', '.gif'}
        if value and Path(value.name).suffix.lower() not in valid_extensions:
            raise serializers.ValidationError(
                'Invalid file extension. Supported extensions are: jpg, jpeg, png, gif'
            )
        return value
