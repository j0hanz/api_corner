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
        request = self.context.get('request')
        return request and request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context.get('request').user
        if user and user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed_user=obj.owner
            ).first()
            return following.id if following else None
        return None
