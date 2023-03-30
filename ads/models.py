from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=2000)
    address = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
