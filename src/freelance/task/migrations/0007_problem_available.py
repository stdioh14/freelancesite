# Generated by Django 3.2.5 on 2021-08-05 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_problem_hidden'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]