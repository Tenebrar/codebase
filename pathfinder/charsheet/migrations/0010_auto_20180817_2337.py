# Generated by Django 2.0.6 on 2018-08-17 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charsheet', '0009_auto_20180817_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterClassLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_level', models.PositiveIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='character',
            name='class_and_level',
        ),
        migrations.AddField(
            model_name='characterclasslevel',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charsheet.Character'),
        ),
        migrations.AddField(
            model_name='characterclasslevel',
            name='character_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='charsheet.CharacterClass'),
        ),
    ]
