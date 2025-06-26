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
        cart=Cart.objects.filter(user=self.request.user)
        cart_items = CartItem.objects.filter(cart=cart[0]).annotate(
            total_amount = models.F('quantity') * models.F('product__price')
        )

        context = super().get_context_data(**kwargs)
        context['title'] = 'VooCommerce | Shopping Cart'
        context['cart_items'] = cart_items

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