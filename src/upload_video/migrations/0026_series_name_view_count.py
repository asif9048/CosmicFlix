# Generated by Django 3.2.24 on 2024-10-10 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_video', '0025_alter_series_name_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='series_name',
            name='view_count',
            field=models.IntegerField(default=0, null=True),
        ),
    ]