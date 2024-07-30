from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    image_url = serializers.ImageField(source='image', read_only=True)

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
            'following_id',
            'followers_count',
            'following_count',
        ]

    def get_is_owner(self, obj):
        """
        Check if the request user is the owner of the profile.
        """
        request = self.context.get('request')
        return request.user == obj.owner if request else False

    def get_following_id(self, obj):
        """
        Get the ID of the following relationship if it exists.
        """
        user = self.context.get('request')
        if user and user.is_authenticated:
            try:
                return Follower.objects.get(owner=user, followed=obj.owner).id
            except Follower.DoesNotExist:
                return None
        return None
