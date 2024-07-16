from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from comments.models import Comment


class Like(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='likes'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes',
        null=True,
        blank=True,
    )
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name='likes',
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('owner', 'post', 'comment')

    def __str__(self):
        if self.post:
            return f'Like {self.id} - Post {self.post.id} by {self.owner.username}'
        elif self.comment:
            return f'Like {self.id} - Comment {self.comment.id} by {self.owner.username}'
        return f'Like {self.id} by {self.owner.username}'
