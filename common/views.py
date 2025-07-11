from celery.worker.state import total_count
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.db import models

from datetime import datetime, timedelta

from rest_framework.reverse import reverse_lazy

from products.models import Category, ProductVariant, Product, Contact
from accounts.models import User, Cart, CartItem
from products.forms import ContactForm


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


class ContactPageView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('common:contact')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


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
        cart=Cart.objects.filter(user=self.request.user)
        cart_items = CartItem.objects.filter(cart=cart[0]).annotate(
            total_amount = models.F('quantity') * models.F('product__price')
        )
        print(cart_items[0].product.images.all()[0].file.url)

        images = cart_items[0].product.images.all()

        cart_data = []

        for cart_item in cart_items:
            cart_item.images = images
            cart_item.total_amount = cart_item.total_amount // 100
            print(cart_item.total_amount)
            if images.exists():
                print(images[0].file.url)
            else:
                print("Нет изображений")

        cart_data.append(
            {
                'product': cart_items[0].product.name,
                'quantity': cart_items[0].quantity,
                'total_amount': cart_items[0].total_amount,
                'images': images[0].file.url,
            }
        )


        context = super().get_context_data(**kwargs)
        context['title'] = 'VooCommerce | Shopping Cart'
        context['cart_items'] = cart_data

        print(cart_data)

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


class SavedProductsPageView(TemplateView):
    template_name = 'saved_products_temolate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'eCommerce | Saved Products'

        # Все сохранённые продукты текущего пользователя
        saved_products = self.request.user.saved_products.all()

        # Находим варианты продуктов, связанных с сохранёнными продуктами
        products = ProductVariant.objects.filter(product__in=saved_products)
        product_data = []
        for variant in products:
            images = variant.images.all()
            if not images.exists():
                images = variant.product.default_images.all()

            print(images[0].file.url)

            product_data.append({
                'variant_name': variant.name,
                'product_name': variant.product.name,
                'price': variant.price,
                'images':  images[0].file,
            })

        context['products'] = product_data

        return context