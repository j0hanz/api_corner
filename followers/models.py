from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Model representing the follower relationship between users.
    """

    follower = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
    )
    followed = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followers',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'followed')
        ordering = ['-created_at']

    def __str__(self):
        """
        Return a string representation of the follower relationship.
        """
        return f"{self.follower} follows {self.followed}"
