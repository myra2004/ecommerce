from rest_framework.generics import DestroyAPIView
from rest_framework import permissions, status
from rest_framework.response import Response

from products.models import Contact


class ContactDeleteAPIView(DestroyAPIView):
    queryset = Contact.objects.all()
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'id'

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()