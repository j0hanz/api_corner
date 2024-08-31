from django.contrib.auth.models import User
from django.db import models

from comments.models import Comment
from posts.models import Post


class Like(models.Model):
    """
    Model representing a like for a post or comment.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes',
        blank=True,
        null=True,
    )
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name='likes',
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner.username} likes {self.post or self.comment}'
