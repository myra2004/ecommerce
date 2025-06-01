from django.views.generic import TemplateView
from django.db import models

from datetime import datetime, timedelta

from products.models import Category, ProductVariant, Product
from accounts.models import User, Cart, CartItem


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = Category.objects.all()
        products = Product.objects.all()
        # latest_products = Product.objects.filter(
        #     created_at =- timedelta(days=1)
        # )
        context['title'] = 'VooCommerce | Home'
        context['categories'] = categories
        context['products'] = products
        # context['latest_products'] = latest_products

        return context


class ContactPageView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'VooCommerce | Contact Us'

        users = User.objects.filter(
            is_staff=False
        )
        context['users'] = users
        return context


class ShopDetailsView(TemplateView):
    template_name = 'shop-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'VooCommerce | Shop Details'

        products = ProductVariant.objects.all()
        context['products'] = products

        return context


class ShopCart(TemplateView):
    template_name = 'shoping-cart.html'

    def get_context_data(self, **kwargs):
        cart_items = CartItem.objects.filter(cart=self.request.user).annotate(
            total_amount = models.F('quantity') * models.F('product__price')
        )
        total_amount = sum(item.total_amount for item in cart_items)

        context = super().get_context_data(**kwargs)
        context['title'] = 'VooCommerce | Shopping Cart'
        context['cart_items'] = cart_items
        context['total_amount'] = total_amount

        return context


class ShopGridView(TemplateView):
    template_name = 'shop-grid.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'VooCommerce | Shop Grid'
        return context


class BlogPageView(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'VooCommerce | Blog Detail'
        return context


class CheckoutPageView(TemplateView):
    template_name = 'checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'VooCommerce | Checkout'
        return context


