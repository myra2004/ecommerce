from django.urls import path

from .apis import *


urlpatterns = [
    path('checkout/', CheckOutAPIView.as_view(), name='checkout'),
]
