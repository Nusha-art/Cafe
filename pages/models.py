from django.db import models
import PIL
from django.urls import reverse

category_menu=(
    ('ВП', 'Выпечка'),
    ('СЛ', 'Салаты'),
    ('ДС', 'Десерты'),
    ('НП', 'Напитки'),
)
class menu(models.Model):
    cost=models.IntegerField(verbose_name="Цена")
    name=models.CharField(max_length=100, verbose_name="Наименование")
    description=models.TextField(verbose_name="Описание")
    image=models.ImageField(verbose_name="Фото")
    category=models.CharField(max_length=2, choices=category_menu, verbose_name="Категория")

    def __str__(self):
        return self.name

class gallery(models.Model):
    image = models.ImageField(verbose_name="Фото")
    name = models.CharField(max_length=100, verbose_name="Наименование")

    def __str__(self):
        return self.name

class team(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(verbose_name="Фото")

    def __str__(self):
        return self.name


class vacancy(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(verbose_name="Фото", blank=True)

    def __str__(self):
        return self.name

class reviews(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    mark = models.FloatField(verbose_name="Оценка", null=True)

    def __str__(self):
        return self.name
# Create your models here.
