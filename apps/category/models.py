from distutils.command.upload import upload
from pyexpat import model
from tabnanny import verbose
from turtle import title
from unicodedata import name
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Actor(models.Model):
    title = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to="actors/")


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('actor_detail', kwargs={"slug": self.name})

    class Meta:
        verbose_name = "Актеры и режиссеры"
        verbose_name_plural = "Актеры и режиссеры"

class Genre(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
