from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Model representing the follower relationship between users.
    """

    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following'
    )
    followed = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followers'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['follower', 'followed'],
                name='unique_follower_followed',
            )
        ]
        ordering = ['-created_at']
        verbose_name = 'Follower'
        verbose_name_plural = 'Followers'

    def __str__(self):
        return f'{self.follower.username} follows {self.followed.username}'
