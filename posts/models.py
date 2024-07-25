from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Post(models.Model):
    """
    Model representing a post created by a user, with optional image and tags.
    Includes content, owner, and image filter options.
    """

    IMAGE_FILTER_CHOICES = [
        ('_1977', '1977'),
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'),
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'),
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'),
        ('normal', 'Normal'),
        ('nashville', 'Nashville'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'),
        ('valencia', 'Valencia'),
        ('walden', 'Walden'),
        ('xpro2', 'X-pro II'),
    ]

    content = models.TextField(max_length=500)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    image_filter = models.CharField(
        max_length=32, choices=IMAGE_FILTER_CHOICES, default='normal'
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
