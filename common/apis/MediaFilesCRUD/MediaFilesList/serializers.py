from rest_framework import serializers

from common.models import MediaFile


class MediaFileGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ['file']
        read_only_fields = ['id']