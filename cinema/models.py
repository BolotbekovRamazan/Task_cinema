from django.db import models

# Create your models here.

class Actor(models.Model):
    name = models.CharField(max_length=24)
    age = models.IntegerField()
    def __str__(self) -> str:
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    release = models.DateField()
    actors = models.ManyToManyField(Actor)
    def __str__(self) -> str:
        return self.title