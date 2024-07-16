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

    def validate_email(self, value):
        """
        Check that the email field contains a valid email address.
        """
        if '@' not in value:
            raise serializers.ValidationError("Enter a valid email address.")
        return value
