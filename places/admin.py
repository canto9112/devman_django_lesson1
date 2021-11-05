from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Image, Place


class ImageInstanceInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ["preview"]

    def preview(self, obj):
        return format_html("<img src='{}' height=200px />", obj.image.url)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInstanceInline]


class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ['place']
    readonly_fields = ["preview"]

    def preview(self, obj):
        return format_html("<img src='{}' height=200px />", obj.image.url)


admin.site.register(Image, ImageAdmin)

