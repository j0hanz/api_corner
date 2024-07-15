from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comment(models.Model):
    """
    Model for users to comment on posts.
    """

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return (
            f'Comment {self.id} on Post {self.post.id} by {self.user.username}'
        )
