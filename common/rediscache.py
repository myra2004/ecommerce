from django.core.cache import cache
from rest_framework.response import Response

from core.constants import cache_time


class RedisCacheMixin:
    cache_time_out = cache_time
    cache_key = None
    print('cache rabotayt')

    def list(self, request, *args, **kwargs):
        if not self.cache_key:
            return super().list(request, *args, **kwargs)

        cached_data = cache.get(self.cache_key)
        if cached_data:
            print(f"Using Redis cache: {self.cache_key}")
            return Response(cached_data)

        response = super().list(request, *args, **kwargs)
        cache.set(self.cache_key, response.data, timeout=self.cache_time_out)
        return response