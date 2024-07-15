from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class FavoriteMusicGenre(models.Model):
    GENRE_CHOICES = [
        ("Rock", _("Rock")),
        ("Pop", _("Pop")),
        ("Jazz", _("Jazz")),
        ("Classical", _("Classical")),
        ("Hip-hop", _("Hip-hop")),
        ("Country", _("Country")),
        ("Electronic", _("Electronic")),
        ("Blues", _("Blues")),
        ("Reggae", _("Reggae")),
        ("Soul", _("Soul")),
        ("Metal", _("Metal")),
        ("Folk", _("Folk")),
        ("Punk", _("Punk")),
        ("R&B", _("R&B")),
        ("Latin", _("Latin")),
        ("Alternative", _("Alternative")),
        ("Other", _("Other")),
    ]

    genre = models.CharField(
        max_length=50,
        choices=GENRE_CHOICES,
        verbose_name=_("Genre"),
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("Favorite Music Genre")
        verbose_name_plural = _("Favorite Music Genres")
        ordering = ["genre"]

    def __str__(self):
        return self.genre


class FavoriteSport(models.Model):
    SPORT_CHOICES = [
        ("Soccer", _("Soccer")),
        ("Basketball", _("Basketball")),
        ("Baseball", _("Baseball")),
        ("Football", _("Football")),
        ("Tennis", _("Tennis")),
        ("Golf", _("Golf")),
        ("Swimming", _("Swimming")),
        ("Cycling", _("Cycling")),
        ("Running", _("Running")),
        ("Volleyball", _("Volleyball")),
        ("Boxing", _("Boxing")),
        ("Cricket", _("Cricket")),
        ("Hockey", _("Hockey")),
        ("Rugby", _("Rugby")),
        ("Surfing", _("Surfing")),
        ("Skateboarding", _("Skateboarding")),
        ("Skiing", _("Skiing")),
        ("Snowboarding", _("Snowboarding")),
        ("Climbing", _("Climbing")),
        ("Martial Arts", _("Martial Arts")),
        ("Other", _("Other")),
    ]

    sport = models.CharField(
        max_length=50,
        choices=SPORT_CHOICES,
        verbose_name=_("Sport"),
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("Favorite Sport")
        verbose_name_plural = _("Favorite Sports")
        ordering = ["sport"]

    def __str__(self):
        return self.sport


class FavoriteMovieGenre(models.Model):
    GENRE_CHOICES = [
        ("Action", _("Action")),
        ("Comedy", _("Comedy")),
        ("Drama", _("Drama")),
        ("Horror", _("Horror")),
        ("Romance", _("Romance")),
        ("Thriller", _("Thriller")),
        ("Science Fiction", _("Science Fiction")),
        ("Fantasy", _("Fantasy")),
        ("Documentary", _("Documentary")),
        ("Animation", _("Animation")),
        ("Adventure", _("Adventure")),
        ("Mystery", _("Mystery")),
        ("Crime", _("Crime")),
        ("Musical", _("Musical")),
        ("Western", _("Western")),
        ("Other", _("Other")),
    ]

    genre = models.CharField(
        max_length=50,
        choices=GENRE_CHOICES,
        verbose_name=_("Genre"),
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("Favorite Movie Genre")
        verbose_name_plural = _("Favorite Movie Genres")
        ordering = ["genre"]

    def __str__(self):
        return self.genre


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    favorite_movie_genre = models.ForeignKey(
        FavoriteMovieGenre,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Favorite Movie Genre"),
    )
    favorite_music_genre = models.ForeignKey(
        FavoriteMusicGenre,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Favorite Music Genre"),
    )
    favorite_sport = models.ForeignKey(
        FavoriteSport,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Favorite Sport"),
    )
    image = models.ImageField(
        upload_to='images/',
        default='images/default_profile.png',
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
