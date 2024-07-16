# Generated by Django 5.0.7 on 2024-07-16 12:19

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
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('category', models.CharField(choices=[('update', 'Update'), ('general_news', 'General News'), ('important', 'Important')], max_length=50)),
                ('published_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'News Article',
                'verbose_name_plural': 'News Articles',
                'ordering': ['-published_at'],
            },
        ),
    ]
