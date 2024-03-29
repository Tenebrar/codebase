# Generated by Django 2.0.6 on 2018-07-12 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('base_strength', models.PositiveIntegerField(default=10)),
                ('base_constitution', models.PositiveIntegerField(default=10)),
                ('base_dexterity', models.PositiveIntegerField(default=10)),
                ('base_intelligence', models.PositiveIntegerField(default=10)),
                ('base_wisdom', models.PositiveIntegerField(default=10)),
                ('base_charisma', models.PositiveIntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Roll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('die_size', models.PositiveIntegerField()),
                ('result', models.PositiveIntegerField()),
                ('reason', models.CharField(max_length=200)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charsheet.Character')),
            ],
        ),
    ]
