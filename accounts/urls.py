from django.urls import path
from django.views.generic import FormView

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
    PasswordResetConfirmAPIView,
    VerifyEmailView,
    RegisterView, SaveProductAPIView, SavedProductListAPIView
)
from products.api_endpoints import UserReviewsListAPIView, UserCommentsListAPIView
from .views import *
from .template_views import *

urlpatterns = [
    path('login/', SessionLoginAPIView.as_view(), name="login-session"),
    path('logout/', SessionLogoutAPIView.as_view(), name="logout-session"),
    path('cart-items/', CartItemListAPIView.as_view(), name='cart-items'),
    path('cart/cart_items/create/', CartItemCreateAPIView.as_view(), name='cart-item-create'),
    path('cart/cart_items/delete/<int:pk>/', CartItemDeleteAPIView.as_view(), name='cart-item-delete'),
    path('cart/cart_items/update/<int:pk>/', CartItemUpdateAPIView.as_view(), name='cart-item-update'),

    # Profile
    path('profile/update/', ProfileUpdateAPIView.as_view(), name='profile-update'),
    path('profile/delete/<int:pk>/', ProfileDeleteAPIView.as_view(), name='profile-update'),

    path('password-reset/', RequestPasswordResetView.as_view(), name="password-reset"),
    path('password-reset/confirm/', PasswordResetConfirmAPIView.as_view(), name="password-reset-confirm"),
    path('verify-email/', VerifyEmailView.as_view(), name="verify-email"),
    path('register/', RegisterView.as_view(), name="register"),

    # Reviews, Comments
    path('profile/reviews/', UserReviewsListAPIView.as_view(), name='user-reviews'),
    path('profile/comments/', UserCommentsListAPIView.as_view(), name='user-comments'),

    # Saved Products
    path('product/save-unsave', SaveProductAPIView.as_view(), name='save-unsave-product'),

    #template_views
    path("template/register/", RegisterTemplateView.as_view(), name="register-template"),
    path("template/login/", LoginTemplateView.as_view(), name="login-template"),
    path("template/profile/", ProfileTemplateView.as_view(), name="profile-template"),

    # Saved Products
    path('saved_products/', SavedProductListAPIView.as_view(), name='saved-products'),
    path('saved_products/create/', SaveProductAPIView.as_view(), name='saved-product-create'),
]