from django.contrib import admin

from common.models import MediaFile


@admin.register(MediaFile)
class MedialFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file')