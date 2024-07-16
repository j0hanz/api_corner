# Generated by Django 5.0.7 on 2024-07-16 18:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='category',
            field=models.CharField(choices=[('general', 'General Inquiry'), ('feedback', 'Feedback'), ('support', 'Support')], max_length=20),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=100, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=100),
        ),
    ]
