from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Follower model, representing the follower relationship between users.
    """

    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        User, related_name='followers', on_delete=models.CASCADE
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
