# Generated by Django 5.0.7 on 2024-07-24 15:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bookmarks', '0001_initial'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookmarked_by', to='posts.post'),
        ),
        migrations.AlterUniqueTogether(
            name='bookmark',
            unique_together={('owner', 'post')},
        ),
    ]
