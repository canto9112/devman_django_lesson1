from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Image, Place


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInstanceInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ['place']
    readonly_fields = ["preview"]

    def preview(self, obj):
        return format_html("<img src='{}' height=200px />", obj.image.url)


class ImageInstanceInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ["preview"]

    def preview(self, obj):
        return format_html("<img src='{}' height=200px />", obj.image.url)

