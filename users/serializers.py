from rest_framework import serializers
from .models import Profile
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
            'id',
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
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']

    def get_is_owner(self, obj):
        """
        Check if the request user is the owner of the profile.
        """
        request = self.context.get('request')
        return request and request.user == obj.owner

    def update(self, instance, validated_data):
        """
        Update profile and handle image replacement.
        """
        new_image = validated_data.get('image')
        if new_image and instance.image:
            try:
                instance.image.delete(save=False)
            except Exception as e:
                logger.error(f"Error deleting old image: {e}")

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
