from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = News
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'author',
            'category',
            'published_at',
            'updated_at',
        ]

    def validate(self, data):
        request = self.context.get('request', None)
        if request and not request.user.is_superuser:
            raise serializers.ValidationError(
                "Only superusers can create news articles."
            )
        return data
