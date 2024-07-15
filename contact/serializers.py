from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Contact
        fields = [
            'id',
            'user',
            'category',
            'subject',
            'message',
            'created_at',
        ]
