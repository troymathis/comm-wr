# Generated by Django 4.0.5 on 2022-07-12 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(max_length=250)),
                ('instagram', models.CharField(default='@', max_length=30)),
                ('twitter', models.CharField(default='@', max_length=30)),
                ('psn', models.CharField(max_length=30)),
                ('xbox', models.CharField(max_length=30)),
                ('steam', models.CharField(max_length=30)),
                ('interests', models.ManyToManyField(to='main_app.interest')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='profpic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.person')),
            ],
        ),
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.interest')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
