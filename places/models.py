from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):

    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description_short = models.TextField(verbose_name='Короткое описание')
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')
    content = HTMLField(null=True, verbose_name='Содержание')

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images', verbose_name='Место')
    image = models.ImageField(verbose_name='Изображение')
    img_number = models.IntegerField(verbose_name='Номер изображения ')

    def __str__(self):
        return f'{self.img_number} {str(self.place)}'

    class Meta:
        ordering = ["img_number"]








