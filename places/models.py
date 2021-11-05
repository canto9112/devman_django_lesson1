from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):

    title = models.CharField(max_length=200, verbose_name='Заголовок', null=True)
    description_short = models.TextField(verbose_name='Короткое описание', null=True, blank=True)
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')
    content = HTMLField(null=True, verbose_name='Содержание', blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images', verbose_name='Место')
    image = models.ImageField(verbose_name='Изображение')
    number = models.IntegerField(verbose_name='Номер изображения', db_index=True, blank=True)

    def __str__(self):
        return f'{self.number} {str(self.place)}'

    class Meta:
        ordering = ["number"]








