# Generated by Django 2.0.6 on 2018-08-17 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charsheet', '0010_auto_20180817_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterclasslevel',
            name='character_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='levels', to='charsheet.CharacterClass'),
        ),
    ]
