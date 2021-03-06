from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from places.views import get_place_view, index

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', index),
        path('tinymce/', include('tinymce.urls')),
        path('<int:place_id>/', get_place_view, name='place_view')
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
