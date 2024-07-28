from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from cloudinary.models import CloudinaryField


class Post(models.Model):
    """
    Model representing a post created by a user, with optional image and tags.
    Includes content, owner, and image filter options.
    """

    IMAGE_FILTER_CHOICES = [
        ('NONE', 'None'),
        ('GRAYSCALE', 'Grayscale'),
        ('SEPIA', 'Sepia'),
        ('NEGATIVE', 'Negative'),
        ('BRIGHTNESS', 'Brightness'),
        ('CONTRAST', 'Contrast'),
    ]
    DEFAULT_IMAGE_FILTER = 'NONE'

    content = models.TextField(max_length=500)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )
    image = CloudinaryField('image', blank=True, null=True)
    image_filter = models.CharField(
        max_length=20,
        choices=IMAGE_FILTER_CHOICES,
        default=DEFAULT_IMAGE_FILTER,
    )
    tags = TaggableManager(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return f'Post {self.id} by {self.owner.username}'
