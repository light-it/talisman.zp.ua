from django.contrib import admin
from .models import Gallery, GalleryImage, Category


class ImageInline(admin.StackedInline):
    model = GalleryImage


class GalleryAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Category, CategoryAdmin)
