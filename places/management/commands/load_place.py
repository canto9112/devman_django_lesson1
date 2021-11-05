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
        place_raw = place_response.json()
        place, created = Place.objects.get_or_create(
            title=place_raw['title'],
            defaults={
                'title': place_raw['title'],
                'description_short': place_raw['description_short'],
                'content': place_raw['description_long'],
                'lng': place_raw['coordinates']['lng'],
                'lat': place_raw['coordinates']['lat']
            },
        )
        if not created:
            return
        
        for img_number, img_url in enumerate(place_json['imgs'], start=1):
            img_response = requests.get(img_url)
            img_response.raise_for_status()
            filename = os.path.basename(img_url)
            picture = Image.objects.create(place=place, img_number=img_number)
            picture.image.save(filename, ContentFile(BytesIO(img_response.content).getvalue()), save=False)
            picture.save()
