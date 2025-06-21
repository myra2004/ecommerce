from rest_framework.generics import ListAPIView

from products.models import Product, Story
from .serializer import StoryListSerializer


class StoryListAPIView(ListAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryListSerializer