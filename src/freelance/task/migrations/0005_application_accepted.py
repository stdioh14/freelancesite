# Generated by Django 3.2.5 on 2021-08-03 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_auto_20210802_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
    ]