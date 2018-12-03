# Generated by Django 2.0.6 on 2018-08-22 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charsheet', '0026_auto_20180822_0146'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=32)),
                ('source_type', models.CharField(max_length=32)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charsheet.Character')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charsheet.Skill')),
            ],
        ),
    ]
