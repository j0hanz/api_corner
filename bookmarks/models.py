from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Bookmark(models.Model):
    """
    Model for users to bookmark specific posts.
    """

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookmarks'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='bookmarked_by'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('owner', 'post')
        ordering = ['-created_at']
        verbose_name = 'Bookmark'
        verbose_name_plural = 'Bookmarks'

    def __str__(self):
        return f'Bookmark by {self.owner.username} for Post {self.post.id}'
