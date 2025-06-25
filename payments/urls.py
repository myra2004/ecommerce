from django.urls import path

from .apis import *


urlpatterns = [
    # WooPay
    path('woopay/create/', WooPayCreateAPIView.as_view(), name='woo-pay-create'),
    path('woopay/perform/', WooPayPerformAPIView.as_view(), name='woo-pay-perform')
]