from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from cloudinary.models import CloudinaryField


class Post(models.Model):
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

    content = models.TextField(max_length=500, verbose_name='Content')
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name='Owner',
    )
    image = CloudinaryField('image', blank=True, verbose_name='Image')
    image_filter = models.CharField(
        max_length=32,
        choices=IMAGE_FILTER_CHOICES,
        default='normal',
        verbose_name='Image Filter',
    )
    tags = TaggableManager(blank=True, verbose_name='Tags')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Created At'
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return f'Post {self.id} by {self.owner.username}'
