# Generated by Django 4.2.5 on 2023-11-04 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload_video', '0023_login_password_alter_login_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='login',
        ),
    ]