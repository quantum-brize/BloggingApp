# Generated by Django 3.0.6 on 2020-06-26 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0015_auto_20200627_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article',
            field=models.TextField(max_length=10000, primary_key=True, serialize=False),
        ),
    ]