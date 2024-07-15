# Generated by Django 5.0.7 on 2024-07-15 20:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteMovieGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(blank=True, choices=[('Action', 'Action'), ('Comedy', 'Comedy'), ('Drama', 'Drama'), ('Horror', 'Horror'), ('Romance', 'Romance'), ('Thriller', 'Thriller'), ('Science Fiction', 'Science Fiction'), ('Fantasy', 'Fantasy'), ('Documentary', 'Documentary'), ('Animation', 'Animation'), ('Adventure', 'Adventure'), ('Mystery', 'Mystery'), ('Crime', 'Crime'), ('Musical', 'Musical'), ('Western', 'Western'), ('Other', 'Other')], max_length=50, null=True, verbose_name='Genre')),
            ],
            options={
                'verbose_name': 'Favorite Movie Genre',
                'verbose_name_plural': 'Favorite Movie Genres',
                'ordering': ['genre'],
            },
        ),
        migrations.CreateModel(
            name='FavoriteMusicGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(blank=True, choices=[('Rock', 'Rock'), ('Pop', 'Pop'), ('Jazz', 'Jazz'), ('Classical', 'Classical'), ('Hip-hop', 'Hip-hop'), ('Country', 'Country'), ('Electronic', 'Electronic'), ('Blues', 'Blues'), ('Reggae', 'Reggae'), ('Soul', 'Soul'), ('Metal', 'Metal'), ('Folk', 'Folk'), ('Punk', 'Punk'), ('R&B', 'R&B'), ('Latin', 'Latin'), ('Alternative', 'Alternative'), ('Other', 'Other')], max_length=50, null=True, verbose_name='Genre')),
            ],
            options={
                'verbose_name': 'Favorite Music Genre',
                'verbose_name_plural': 'Favorite Music Genres',
                'ordering': ['genre'],
            },
        ),
        migrations.CreateModel(
            name='FavoriteSport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport', models.CharField(blank=True, choices=[('Soccer', 'Soccer'), ('Basketball', 'Basketball'), ('Baseball', 'Baseball'), ('Football', 'Football'), ('Tennis', 'Tennis'), ('Golf', 'Golf'), ('Swimming', 'Swimming'), ('Cycling', 'Cycling'), ('Running', 'Running'), ('Volleyball', 'Volleyball'), ('Boxing', 'Boxing'), ('Cricket', 'Cricket'), ('Hockey', 'Hockey'), ('Rugby', 'Rugby'), ('Surfing', 'Surfing'), ('Skateboarding', 'Skateboarding'), ('Skiing', 'Skiing'), ('Snowboarding', 'Snowboarding'), ('Climbing', 'Climbing'), ('Martial Arts', 'Martial Arts'), ('Other', 'Other')], max_length=50, null=True, verbose_name='Sport')),
            ],
            options={
                'verbose_name': 'Favorite Sport',
                'verbose_name_plural': 'Favorite Sports',
                'ordering': ['sport'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255)),
                ('bio', models.TextField(blank=True)),
                ('image', models.ImageField(default='images/default_profile.png', upload_to='images/')),
                ('location', models.CharField(blank=True, max_length=100)),
                ('url_link', models.URLField(blank=True)),
                ('contact_email', models.EmailField(blank=True, max_length=254)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('favorite_movie_genre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.favoritemoviegenre', verbose_name='Favorite Movie Genre')),
                ('favorite_music_genre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.favoritemusicgenre', verbose_name='Favorite Music Genre')),
                ('favorite_sport', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.favoritesport', verbose_name='Favorite Sport')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
