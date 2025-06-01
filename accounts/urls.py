from django.urls import path

from accounts.api_endpoints import (
    CartItemListAPIView,
    CartItemCreateAPIView,
    CartItemUpdateAPIView,
    CartItemDeleteAPIView,
    SessionLoginAPIView,
    SessionLogoutAPIView,
    ProfileUpdateAPIView,
    ProfileDeleteAPIView,
    RequestPasswordResetView,
    PasswordResetConfirmAPIView
)

urlpatterns = [
    path('login/', SessionLoginAPIView.as_view(), name="login-session"),
    path('logout/', SessionLogoutAPIView.as_view(), name="logout-session"),
    path('cart-items/', CartItemListAPIView.as_view(), name='cart-items'),
    path('cart/cart_items/create/', CartItemCreateAPIView.as_view(), name='cart-item-create'),
    path('cart/cart_items/delete/<int:pk>/', CartItemDeleteAPIView.as_view(), name='cart-item-delete'),
    path('cart/cart_items/update/<int:pk>/', CartItemUpdateAPIView.as_view(), name='cart-item-update'),

    # Profile
    path('profile/update/', ProfileUpdateAPIView.as_view(), name='profile-update'),
    path('profile/delete/', ProfileDeleteAPIView.as_view(), name='profile-update'),

    path('password-reset/', RequestPasswordResetView.as_view(), name="password-reset"),
    path('password-reset/confirm/', PasswordResetConfirmAPIView.as_view(), name="password-reset-confirm"),
]