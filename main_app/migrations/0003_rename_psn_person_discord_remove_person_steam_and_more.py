# Generated by Django 4.0.5 on 2022-07-13 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_person_hobbies'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='psn',
            new_name='discord',
        ),
        migrations.RemoveField(
            model_name='person',
            name='steam',
        ),
        migrations.RemoveField(
            model_name='person',
            name='xbox',
        ),
    ]
