from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from cloudinary.models import CloudinaryField


class Post(models.Model):
    """
    Post model, representing a post created by a user.
    """

    content = models.TextField(max_length=500)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )
    image = CloudinaryField('image', blank=True, null=True)
    image_filter = models.CharField(
        max_length=20,
        default='NONE',
        choices=[
            ('NONE', 'None'),
            ('GRAYSCALE', 'Grayscale'),
            ('SEPIA', 'Sepia'),
            ('NEGATIVE', 'Negative'),
            ('BRIGHTNESS', 'Brightness'),
            ('CONTRAST', 'Contrast'),
            ('SATURATION', 'Saturation'),
            ('HUE_ROTATE', 'Hue Rotate'),
            ('BLUR', 'Blur'),
            ('SHARPEN', 'Sharpen'),
            ('VINTAGE', 'Vintage'),
            ('VIGNETTE', 'Vignette'),
            ('CROSS_PROCESS', 'Cross Process'),
            ('HDR', 'HDR'),
            ('EDGE_DETECT', 'Edge Detect'),
            ('EMBOSS', 'Emboss'),
            ('SOLARIZE', 'Solarize'),
            ('POSTERIZE', 'Posterize'),
            ('PIXELATE', 'Pixelate'),
            ('CARTOON', 'Cartoon'),
            ('DUOTONE', 'Duotone'),
        ],
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
