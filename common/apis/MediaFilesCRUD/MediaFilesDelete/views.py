from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.generics import DestroyAPIView, GenericAPIView

from products.models import MediaFile


class MediaFileDeleteAPIView(DestroyAPIView):
    queryset = MediaFile.objects.all()
    permission_classes = (permissions.IsAdminUser)
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        self.perform_destroy(self.get_object())

        return Response({"message": "File deleted successfully"}, status=204)

    def perform_destroy(self, instance):
        if instance.file:
            instance.file.delete(save=False)