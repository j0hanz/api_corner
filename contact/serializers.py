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
        Validate the email field to ensure it contains a valid email address.
        """
        if '@' not in value:
            raise serializers.ValidationError("Enter a valid email address.")
        return value

    def run_validation(self, data=serializers.empty):
        """
        Override run_validation to handle validation errors and remove duplicates.
        """
        try:
            validated_data = super().run_validation(data)
        except serializers.ValidationError as exc:
            exc.detail = self._remove_duplicate_errors(exc.detail)
            raise exc
        return validated_data

    def _remove_duplicate_errors(self, errors):
        """
        Remove duplicate error messages from the errors dictionary.
        """
        if isinstance(errors, dict):
            for field, messages in errors.items():
                if isinstance(messages, list):
                    errors[field] = list(set(messages))
        return errors
