# Generated by Django 4.1 on 2022-08-23 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_list_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='list',
            options={},
        ),
        migrations.RemoveField(
            model_name='list',
            name='complete',
        ),
    ]
