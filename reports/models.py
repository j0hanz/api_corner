from django.contrib.auth.models import User
from django.db import models

from comments.models import Comment
from posts.models import Post


class Report(models.Model):
    """Model for users to report inappropriate posts, comments, or users."""

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
    reason = models.TextField()
    reported_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-reported_at']

    def __str__(self):
        """Return a string representation of the Report object."""
        report_details = []
        if self.post:
            report_details.append(f'Post {self.post.id}')
        if self.comment:
            report_details.append(f'Comment {self.comment.id}')
        if self.reported_user:
            report_details.append(f'User {self.reported_user.username}')

        details = ' - '.join(report_details) if report_details else 'General'
        return f'Report {self.id} - {details} by {self.owner.username}'
