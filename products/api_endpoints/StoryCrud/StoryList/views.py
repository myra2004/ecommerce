from rest_framework.generics import ListAPIView

from products.models import Product, Story
from .serializer import StoryListSerializer
from common.rediscache import RedisCacheMixin


class StoryListAPIView(RedisCacheMixin, ListAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryListSerializer
    cache_key = 'story-list'