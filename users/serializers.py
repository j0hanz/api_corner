from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            'id',
            'owner',
            'first_name',
            'last_name',
            'bio',
            'image',
            'image_url',
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
        read_only_fields = [
            'id',
            'owner',
            'created_at',
            'updated_at',
            'image_url',
        ]

    def get_is_owner(self, obj):
        """
        Check if the request user is the owner of the profile.
        """
        request = self.context.get('request')
        return request and request.user == obj.owner

    def get_image_url(self, obj):
        """
        Get the URL of the profile image.
        """
        return obj.image.url if obj.image else None
