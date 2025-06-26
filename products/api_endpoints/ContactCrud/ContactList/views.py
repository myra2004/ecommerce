from rest_framework.generics import ListAPIView
from rest_framework import permissions

from products.models import Contact
from .serializer import ContactListSerializer
from common.rediscache import RedisCacheMixin


class ContactListAPIView(RedisCacheMixin, ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListSerializer
    cache_key = 'contact-list'
    permission_classes = [permissions.IsAuthenticated]