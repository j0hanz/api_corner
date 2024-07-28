from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model.
    Includes logic to prevent duplicate likes.
    """

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = ['id', 'owner', 'post', 'comment', 'created_at']

    def validate(self, data):
        """
        Ensure that either post or comment is provided, but not both.
        """
        post = data.get('post')
        comment = data.get('comment')

        if not post and not comment:
            raise serializers.ValidationError(
                'Either post or comment must be provided.'
            )
        if post and comment:
            raise serializers.ValidationError(
                'Only one of post or comment should be provided.'
            )

        return data

    def create(self, validated_data):
        """
        Creates a Like instance.
        Checks if the user already liked the post or comment.
        Throws an error if the user already liked that instance.
        """
        owner = self.context['request'].user
        post = validated_data.get('post')
        comment = validated_data.get('comment')

        if Like.objects.filter(
            owner=owner, post=post, comment=comment
        ).exists():
            raise serializers.ValidationError('You already liked this')

        validated_data['owner'] = owner
        return super().create(validated_data)
