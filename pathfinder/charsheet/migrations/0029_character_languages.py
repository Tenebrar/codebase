# Generated by Django 2.0.6 on 2018-08-22 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charsheet', '0028_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='languages',
            field=models.ManyToManyField(blank=True, null=True, to='charsheet.Language'),
        ),
    ]
