# Generated by Django 2.1.1 on 2018-09-18 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winspool', '0004_auto_20180917_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='week',
            name='season',
            field=models.IntegerField(default=2018),
        ),
    ]
