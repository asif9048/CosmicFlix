# Generated by Django 4.2.5 on 2023-10-25 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mylist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_list', models.CharField(max_length=20)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
