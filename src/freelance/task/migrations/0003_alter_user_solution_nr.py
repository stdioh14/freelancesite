# Generated by Django 3.2.5 on 2021-08-02 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20210802_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='solution_nr',
            field=models.IntegerField(default=0),
        ),
    ]
