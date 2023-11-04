from django.db import models
from django.contrib.auth.models import User

class Category (models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Shelf (models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Book (models.Model):
    name = models.CharField(max_length=225)
    author = models.CharField(max_length=225)
    book = models.FileField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    shelf = models.ForeignKey(to=Shelf, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name