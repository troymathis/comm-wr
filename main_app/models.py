from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Interest(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Hobbies(models.Model):
    name = models.CharField(max_length=30)
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=250)
    instagram = models.CharField(max_length=30, default = '@')
    twitter = models.CharField(max_length=30, default = '@')
    discord = models.CharField(max_length=30)
    interests = models.ManyToManyField(Interest)
    hobbies = models.ManyToManyField(Hobbies)

class profpic(models.Model):
    url = models.CharField(max_length=200)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)