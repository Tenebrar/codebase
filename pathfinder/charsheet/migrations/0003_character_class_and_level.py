# Generated by Django 2.0.6 on 2018-08-08 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charsheet', '0002_auto_20180808_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='class_and_level',
            field=models.CharField(default='', max_length=256),
        ),
    ]
