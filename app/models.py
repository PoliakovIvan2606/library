from django.db import models

class Category (models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book (models.Model):
    name = models.CharField(max_length=225)
    author = models.CharField(max_length=225)
    book = models.FileField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name