# Generated by Django 2.0.6 on 2018-08-21 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charsheet', '0023_auto_20180822_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='climb_speed',
            field=models.PositiveIntegerField(default=0, help_text='expressed in feet'),
        ),
    ]
