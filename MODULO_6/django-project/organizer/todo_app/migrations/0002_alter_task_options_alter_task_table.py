# Generated by Django 5.0.6 on 2024-05-31 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
        migrations.AlterModelTable(
            name='task',
            table='task',
        ),
    ]
