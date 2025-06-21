from django.urls import path

from .views import HomePageView, ContactPageView, ShopDetailsView, ShopCart, ShopGridView, CheckoutPageView, BlogPageView
from .apis import *


app_name = 'common'

urlpatterns = [

    # templates
    path('index/', HomePageView.as_view(), name='home'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('shop-details/', ShopDetailsView.as_view(), name='shop-details'),
    path('shop-cart/', ShopCart.as_view(), name='shop-cart'),
    path('shop-grid/', ShopGridView.as_view(), name='shop-grid'),
    path('checkout/', CheckoutPageView.as_view(), name='checkout'),
    path('blog/', BlogPageView.as_view(), name='blog'),

    # Media CRUD
    path('mediafiles/list/', MediaFileGetAPIView.as_view(), name='category-list'),
    path('mediafiles/create/', MediaFileCreateAPIView.as_view(), name='category-create'),
    path('mediafiles/delete/<int:id>/', MediaFileDeleteAPIView.as_view(), name='category-delete'),
]