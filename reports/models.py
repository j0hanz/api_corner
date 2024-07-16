from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from comments.models import Comment


class Report(models.Model):
    """
    Model for users to report inappropriate posts, comments, or users.
    """

    owner = models.ForeignKey(
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
    reported_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reported_by',
        null=True,
        blank=True,
    )
    reason = models.TextField(blank=False)
    reported_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-reported_at']

    def __str__(self):
        if self.post:
            return f'Report {self.id} - Post {self.post.id} by {self.owner.username}'
        elif self.comment:
            return f'Report {self.id} - Comment {self.comment.id} by {self.owner.username}'
        elif self.reported_user:
            return f'Report {self.id} - User {self.reported_user.username} by {self.owner.username}'
        return f'Report {self.id} by {self.owner.username}'
