from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Place


def serialize_place(place):
    return {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lng, place.lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.pk,
                    "detailsUrl": reverse('place_view', args=[place.pk])
                }
            }]
    }


def index(request):
    all_places = Place.objects.all()
    context = {
        'all_places': [serialize_place(place) for place in all_places]
    }
    return render(request, "index.html", context)


def get_place_view(request, place_id):
    current_place = get_object_or_404(Place, pk=place_id)

    response = {
        'title': current_place.title,
        'imgs': [image.image.url for image in current_place.images.all()],
        'lat': current_place.lat,
        'description_short': current_place.description_short,
        'description_long': current_place.content,
        'coordinates': {
            'lat': current_place.lat,
            'lng': current_place.lng
        }
    }
    return JsonResponse(response, safe=False,
                        json_dumps_params={'ensure_ascii': False, 'indent': 2})
