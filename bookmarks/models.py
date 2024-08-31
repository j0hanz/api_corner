from django.contrib.auth.models import User
from django.db import models

from posts.models import Post


class Bookmark(models.Model):
    """
    Bookmark model, representing a bookmark created by a user.
    """

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookmarks'
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['owner', 'post'], name='unique_bookmark'
            )
        ]

    def __str__(self):
        return f'{self.owner} bookmarked {self.post}'
