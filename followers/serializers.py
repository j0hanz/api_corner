from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Follower model.
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    followed_user = serializers.ReadOnlyField(source='followed_user.username')

    class Meta:
        model = Follower
        fields = ['id', 'owner', 'followed_user', 'created_at']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})
