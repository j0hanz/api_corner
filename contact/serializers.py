from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'id',
            'owner',
            'category',
            'email',
            'subject',
            'message',
            'created_at',
        ]
        read_only_fields = ['owner', 'created_at']
