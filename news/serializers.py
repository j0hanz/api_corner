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
