# Generated by Django 3.2.5 on 2021-08-02 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.user'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.user'),
        ),
    ]
