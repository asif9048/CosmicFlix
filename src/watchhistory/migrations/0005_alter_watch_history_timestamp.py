# Generated by Django 4.2.5 on 2023-10-30 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchhistory', '0004_alter_watch_history_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watch_history',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]