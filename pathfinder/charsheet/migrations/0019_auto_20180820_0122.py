# Generated by Django 2.0.6 on 2018-08-19 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charsheet', '0018_conditionalmodifier'),
    ]

    operations = [
        migrations.AddField(
            model_name='conditionalmodifier',
            name='source',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='conditionalmodifier',
            name='source_type',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
    ]
