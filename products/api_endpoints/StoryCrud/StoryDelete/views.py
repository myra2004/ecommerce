from rest_framework.generics import DestroyAPIView
from rest_framework import permissions, status
from rest_framework.response import Response

from products.models import Product, Story


class StoryDeleteView(DestroyAPIView):
    queryset = Story.objects.all()
    # permission_classes = [permissions.IsAdminUser]
    lookup_field = 'id'

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
        return Response({'detail': 'This story has been deleted'}, status=status.HTTP_200_OK)