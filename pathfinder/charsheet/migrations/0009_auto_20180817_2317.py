# Generated by Django 2.0.6 on 2018-08-17 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charsheet', '0008_auto_20180811_1457'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bonus',
            options={'verbose_name_plural': 'Bonuses'},
        ),
        migrations.AddField(
            model_name='character',
            name='copper',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='gold',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='platinum',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='silver',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
