import os
import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from io import BytesIO
from places.models import Image, Place


class Command(BaseCommand):
    help = 'Добавить места из ссылки на json'

    def add_arguments(self, parser):
        parser.add_argument('place_url', type=str, help='ссылка на json')

    def handle(self, *args, **options):
        place_response = requests.get(options['place_url'])
        place_response.raise_for_status()
        place_json = place_response.json()
        place, created = Place.objects.get_or_create(
            title=place_json['title'],
            defaults={
                'title': place_json['title'],
                'description_short': place_json['description_short'],
                'content': place_json['description_long'],
                'lng': place_json['coordinates']['lng'],
                'lat': place_json['coordinates']['lat']
            },
        )
        if created:
            default_img_number = 0
            for img_url in place_json['imgs']:
                img_response = requests.get(img_url)
                img_response.raise_for_status()
                filename = os.path.basename(img_url)
                default_img_number += 1 
                picture = Image.objects.create(place=place, img_number=default_img_number)
                picture.image.save(filename, ContentFile(BytesIO(img_response.content).getvalue()), save=False)
                picture.save()
        else:
            return
