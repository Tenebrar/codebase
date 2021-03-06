# Generated by Django 2.0.6 on 2018-08-21 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charsheet', '0024_race_climb_speed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Speed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=32)),
                ('speed', models.PositiveIntegerField()),
                ('maneuverability', models.CharField(default='', help_text='only needed for fly speeds', max_length=32)),
                ('source', models.CharField(max_length=32)),
                ('source_type', models.CharField(max_length=32)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charsheet.Character')),
            ],
        ),
    ]
