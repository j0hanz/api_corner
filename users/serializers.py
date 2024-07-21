from rest_framework import serializers
from .models import Profile
from pathlib import Path
from cloudinary.uploader import destroy


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
        request = self.context.get('request')
        return request.user == obj.owner if request else False

    def update(self, instance, validated_data):
        image = validated_data.get('image')
        if image and instance.image:
            destroy(instance.image.public_id)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def validate_image(self, value):
        path = Path(value.name)
        valid_extensions = ['.jpg', '.jpeg', '.png']
        if path.suffix.lower() not in valid_extensions:
            raise serializers.ValidationError(
                'Image must be jpg, jpeg, or png!'
            )
        return value
