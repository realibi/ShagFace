# Generated by Django 3.0.5 on 2020-06-12 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200610_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='face',
            name='absolute_path',
            field=models.TextField(blank=True),
        ),
    ]
