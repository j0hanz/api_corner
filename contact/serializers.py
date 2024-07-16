from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

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
