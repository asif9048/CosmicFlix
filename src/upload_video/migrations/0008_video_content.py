# Generated by Django 4.2.5 on 2023-09-19 08:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('upload_video', '0007_remove_video_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='content',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]