from django.contrib import admin
from .models import gmgallery

# Register your models here.
class gmgalleryAdmin(admin.ModelAdmin):
    list_display = ["title"]

    class Meta:
        model=gmgallery

admin.site.register(gmgallery, gmgalleryAdmin)
