from django.contrib.auth.models import User
from django.db import models


class Follower(models.Model):
    """Represents a follower relationship between users.
    Each instance indicates that 'owner' user is following 'followed'.
    """

    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['owner', 'followed'], name='unique_follow'
            )
        ]

    def __str__(self):
        return f'{self.owner} follows {self.followed}'
