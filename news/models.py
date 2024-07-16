from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.exceptions import ValidationError


class News(models.Model):
    """
    Model representing a news article.
    """

    CATEGORY_UPDATE = 'update'
    CATEGORY_GENERAL_NEWS = 'general_news'
    CATEGORY_IMPORTANT = 'important'

    CATEGORY_CHOICES = [
        (CATEGORY_UPDATE, 'Update'),
        (CATEGORY_GENERAL_NEWS, 'General News'),
        (CATEGORY_IMPORTANT, 'Important'),
    ]

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    content = models.TextField(max_length=3000)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='news_author'
    )
    image = models.ImageField(upload_to='images/', blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_at']
        verbose_name = "News Article"
        verbose_name_plural = "News Articles"

    def __str__(self):
        return self.title

    def clean(self):
        if not self.author.is_superuser:
            raise ValidationError("Only superusers can create news articles.")

    def save(self, *args, **kwargs):
        self.clean()
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
