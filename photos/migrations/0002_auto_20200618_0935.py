# Generated by Django 3.0.6 on 2020-06-18 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='desc',
            new_name='tag',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='price',
        ),
    ]