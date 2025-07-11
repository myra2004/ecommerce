from django.urls import path

from products.api_endpoints import *

urlpatterns = [
    path('list1/', ProductListAPIView1.as_view(), name='product-list1'),
    path('list2/', ProductListAPIView2.as_view(), name='product-list2'),
    path('list3/', ProductListAPIView3.as_view(), name='product-list3'),

    # Category
    path('category/list/', CategoryListAPIView.as_view(), name='category-list'),
    path('category/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('category/update/<int:pk>/', CategoryUpdateAPIView.as_view(), name='category-update'),
    path('category/delete/<int:pk>/', CategoryDeleteAPIView.as_view(), name='category-delete'),

    # Brand
    path('brand/list/', BrandListAPIView.as_view(), name='brand-list'),
    path('brand/create/', BrandCreateAPIView.as_view(), name='brand-create'),
    path('brand/update/<int:pk>/', BrandUpdateAPIView.as_view(), name='brand-update'),
    path('brand/delete/<int:pk>/', BrandDeleteAPIView.as_view(), name='brand-delete'),

    # Color
    path('color/list/', ColorListAPIView.as_view(), name='color-list'),
    path('color/create/', ColorCreateAPIView.as_view(), name='color-create'),
    path('color/update/<int:pk>/', ColorUpdateAPIView.as_view(), name='color-update'),
    path('color/delete/<int:pk>/', ColorDeleteAPIView.as_view(), name='color-delete'),

    # Product Variant
    path('product-variants/list/', ProductVariantListAPIView.as_view(), name='product-variant-list'),
    path('product-variants/create/', ProductVariantCreateAPIView.as_view(), name='product-variant-create'),
    path('product-variants/update/<int:pk>/', ProductVariantUpdateAPIView.as_view(), name='product-variant-update'),
    path('product-variants/delete/<int:pk>/', ProductVariantDeleteAPIView.as_view(), name='product-variant-delete'),

    # Size
    path('size/list/', SizeListAPIView.as_view(), name='size-list'),
    path('size/create/', SizeCreateAPIView.as_view(), name='size-create'),
    path('size/update/<int:pk>/', SizeUpdateAPIView.as_view(), name='size-update'),
    path('size/delete/<int:pk>/', SizeDeleteAPIView.as_view(), name='size-delete'),

    # Review, Comment
    path('review/create/', ReviewCreateAPIView.as_view(), name='review-create'),
    path('review/delete/<int:id>/', ReviewDeleteAPIView.as_view(), name='review-delete'),
    path('comment/create/', CommentCreateAPIView.as_view(), name='comment-create'),
    path('comment/delete/<int:id>/', CommentDeleteAPIView.as_view(), name='comment-delete'),

    # Story
    path('story/create/', StoryCreateAPIView.as_view(), name='story-create'),
    path('story/delete/<int:id>/', StoryDeleteView.as_view(), name='story-delete'),
    path('story/list/', StoryListAPIView.as_view(), name='story-list'),

    # Contact
    path('contact/create/', ContactCreateAPIView.as_view(), name='contact-create'),
    path('contact/list/', ContactListAPIView.as_view(), name='contact-list'),
    path('contact/delete/<int:id>/', ContactDeleteAPIView.as_view(), name='contact-delete'),
]