from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Contact
        fields = '__all__'

    def validate(self, data):
        """
        Validate the email field to ensure it contains a valid email address.
        """
        email = data.get('email')
        if email and '@' not in email:
            raise serializers.ValidationError("Enter a valid email address.")
        return data
