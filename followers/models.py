from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Represents a follower relationship between users.
    Each instance indicates that 'owner' user is following 'followed_user'.
    """

    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
    )
    followed_user = models.ForeignKey(
        User, related_name='followers', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['owner', 'followed_user'], name='unique_follow'
            )
        ]
        verbose_name = 'Follower Relationship'
        verbose_name_plural = 'Follower Relationships'

    def __str__(self):
        return f'{self.owner.username} follows {self.followed_user.username}'
