# Generated by Django 4.1.2 on 2022-10-25 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_history'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='time',
            new_name='timestamp',
        ),
        migrations.RenameField(
            model_name='trending',
            old_name='time',
            new_name='timestamp',
        ),
    ]
