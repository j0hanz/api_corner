from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from comments.models import Comment


class Like(models.Model):
    """
    Model representing a like for a post or comment.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='likes',
    )
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='likes',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['owner', 'post'], name='unique_like_post'
            ),
            models.UniqueConstraint(
                fields=['owner', 'comment'], name='unique_like_comment'
            ),
        ]

    def __str__(self):
        if self.post:
            return f'{self.owner.username} likes {self.post}'
        return f'{self.owner.username} likes {self.comment}'
