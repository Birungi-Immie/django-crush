from turtle import update
from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True ,blank=True)
    update = models.DateField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)