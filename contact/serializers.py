from rest_framework import serializers
from .models import Contact
from datetime import datetime, timezone, timedelta


def shortnaturaltime(value):
    """
    Return a human-readable string representing the time delta from now to the given value.
    """
    now = datetime.now(timezone.utc)
    delta = now - value

    if delta < timedelta(minutes=1):
        return 'just now'
    elif delta < timedelta(hours=1):
        return f'{int(delta.total_seconds() // 60)}m'
    elif delta < timedelta(days=1):
        return f'{int(delta.total_seconds() // 3600)}h'
    else:
        return f'{delta.days}d'


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
