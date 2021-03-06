# Generated by Django 2.1.1 on 2018-09-26 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('winspool', '0005_week_season'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3)),
                ('full_name', models.CharField(max_length=30)),
                ('pick', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='player',
            name='team1',
        ),
        migrations.RemoveField(
            model_name='player',
            name='team2',
        ),
        migrations.RemoveField(
            model_name='player',
            name='team3',
        ),
        migrations.AddField(
            model_name='team',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='winspool.Player'),
        ),
    ]
