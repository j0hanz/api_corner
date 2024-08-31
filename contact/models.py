from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from django.db import models


class Contact(models.Model):
    """
    Model for users to contact us.
    """

    CATEGORY_CHOICES = [
        ('general', 'General Inquiry'),
        ('feedback', 'Feedback'),
        ('support', 'Support'),
    ]

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='contacts'
    )
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, verbose_name='Category'
    )
    email = models.EmailField(
        validators=[EmailValidator()], verbose_name='Email'
    )
    subject = models.CharField(max_length=100, verbose_name='Subject')
    message = models.TextField(verbose_name='Message')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Created at'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Contact {self.id} by {self.owner.username}'
