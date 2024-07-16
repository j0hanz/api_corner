from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class News(models.Model):
    """
    Model representing a news article.
    """

    CATEGORY_CHOICES = [
        ('update', 'Update'),
        ('general_news', 'General News'),
        ('important', 'Important'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='news'
    )
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_at']
        verbose_name = "News Article"
        verbose_name_plural = "News Articles"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
