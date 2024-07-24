from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    owner = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile'
    )
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='images/nobody_ceyo72', blank=True
    )
    location = models.CharField(max_length=100, blank=True)
    url_link = models.URLField(blank=True)
    contact_email = models.EmailField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner.username}'s profile"


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)
