from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from comments.models import Comment


class Report(models.Model):
    """
    Model for users to report inappropriate posts or comments.
    """

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reports'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='reports',
        null=True,
        blank=True,
    )
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name='reports',
        null=True,
        blank=True,
    )
    reason = models.TextField()
    reported_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-reported_at']

    def __str__(self):
        if self.post:
            return f'Report {self.id} - Post {self.post.id} by {self.user.username}'
        elif self.comment:
            return f'Report {self.id} - Comment {self.comment.id} by {self.user.username}'
        return f'Report {self.id} by {self.user.username}'
