from django.db import models
from django.urls import reverse
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
    name = models.CharField(max_length=25, blank=True)
    bio = models.TextField(max_length=250, blank=True)
    instagram = models.CharField(max_length=30, default = '@', blank=True)
    twitter = models.CharField(max_length=30, default = '@', blank=True)
    discord = models.CharField(max_length=30, blank=True)
    interests = models.ManyToManyField(Interest)
    hobbies = models.ManyToManyField(Hobbies)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'person_id': self.id})
    
    def __str__(self):
        return self.name

class profpic(models.Model):
    url = models.CharField(max_length=200)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for person_id: {self.person_id} @{self.url}"