from django.db import models
from django.contrib.auth.models import User
from django.core.validators import EmailValidator


class Contact(models.Model):
    CATEGORY_CHOICES = [
        ('general', 'General Inquiry'),
        ('feedback', 'Feedback'),
        ('support', 'Support'),
    ]

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='contacts'
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    email = models.EmailField(max_length=100, validators=[EmailValidator()])
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Contact {self.id} by {self.owner.username}'
