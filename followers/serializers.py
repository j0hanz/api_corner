from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Follower model.
    """

    follower = serializers.ReadOnlyField(source='follower.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Follower
        fields = ['id', 'follower', 'created_at', 'followed', 'followed_name']

    def create(self, validated_data):
        """
        Creates a Follower instance.
        Raises an error if the relationship already exists.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                {'detail': 'Possible duplicate relationship'}
            )
