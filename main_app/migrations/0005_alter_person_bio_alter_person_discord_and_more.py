# Generated by Django 4.0.5 on 2022-07-14 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_person_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='bio',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='person',
            name='discord',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='person',
            name='instagram',
            field=models.CharField(blank=True, default='@', max_length=30),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='person',
            name='twitter',
            field=models.CharField(blank=True, default='@', max_length=30),
        ),
    ]