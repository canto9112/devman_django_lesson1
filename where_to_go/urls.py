from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from places.views import get_details_url, index

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', index),
        path('tinymce/', include('tinymce.urls')),
        path('<int:place_id>/', get_details_url, name='get_details_url')
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
