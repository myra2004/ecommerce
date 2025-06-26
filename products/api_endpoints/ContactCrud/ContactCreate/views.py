from rest_framework.generics import CreateAPIView

from products.models import Contact
from .serializer import ContactCreateSerializer


class ContactCreateAPIView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactCreateSerializer
    permission_classes = []
