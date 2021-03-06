# Generated by Django 2.0.6 on 2018-08-10 17:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charsheet', '0003_character_class_and_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bonus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to', models.CharField(max_length=32)),
                ('value', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('type', models.CharField(max_length=32)),
                ('source', models.CharField(max_length=32)),
                ('source_type', models.CharField(max_length=32)),
            ],
        ),
        migrations.AlterField(
            model_name='character',
            name='alignment_good_axis',
            field=models.CharField(choices=[('GOOD', 'Good'), ('NEUTRAL', 'Neutral'), ('EVIL', 'Evil')], default='NEUTRAL', max_length=8),
        ),
        migrations.AlterField(
            model_name='character',
            name='alignment_law_axis',
            field=models.CharField(choices=[('LAWFUL', 'Lawful'), ('TRUE', 'True'), ('CHAOTIC', 'Chaotic')], default='TRUE', max_length=8),
        ),
        migrations.AlterField(
            model_name='character',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], default='MALE', max_length=8),
        ),
        migrations.AlterField(
            model_name='character',
            name='size',
            field=models.CharField(choices=[('FINE', 'Fine'), ('DIMINUTIVE', 'Diminutive'), ('TINY', 'Tiny'), ('SMALL', 'Small'), ('MEDIUM', 'Medium'), ('LARGE', 'Large'), ('HUGE', 'Huge'), ('GARGANTUAN', 'Gargantuan'), ('COLOSSAL', 'Colossal')], default='MEDIUM', max_length=16),
        ),
        migrations.AlterField(
            model_name='roll',
            name='die_size',
            field=models.PositiveIntegerField(choices=[(1, 'd1'), (2, 'd2'), (3, 'd3'), (4, 'd4'), (6, 'd6'), (8, 'd8'), (10, 'd10'), (12, 'd12'), (20, 'd20'), (100, 'd100')]),
        ),
        migrations.AlterField(
            model_name='roll',
            name='result',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='bonus',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charsheet.Character'),
        ),
    ]
