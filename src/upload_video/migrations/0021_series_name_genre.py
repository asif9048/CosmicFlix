# Generated by Django 4.2.5 on 2023-10-12 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_video', '0020_alter_series_name_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='series_name',
            name='genre',
            field=models.CharField(max_length=30, null=True),
        ),
    ]