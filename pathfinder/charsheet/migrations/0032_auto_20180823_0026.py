# Generated by Django 2.0.6 on 2018-08-22 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charsheet', '0031_auto_20180823_0003'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weaponproperty',
            options={'verbose_name_plural': 'Weapon properties'},
        ),
        migrations.AlterField(
            model_name='note',
            name='value',
            field=models.CharField(default='', max_length=256),
        ),
    ]
