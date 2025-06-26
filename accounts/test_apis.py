from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

from accounts.models import Cart, CartItem
from products.models import Product, ProductVariant

User = get_user_model()

class LoginAPITests(TestCase):
    """Тесты для API авторизации"""
    
    def setUp(self):
        """Настройка перед каждым тестом"""
        self.client = APIClient()
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpassword',
            username='testuser'
        )
        self.login_url = reverse('accounts:login')
        
    def test_user_login(self):
        """Тест успешного входа"""
        data = {
            'email': 'test@example.com',
            'password': 'testpassword'
        }
        
        response = self.client.post(self.login_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        
    def test_invalid_credentials(self):
        """Тест входа с неверными учетными данными"""
        data = {
            'email': 'test@example.com',
            'password': 'wrongpassword'
        }
        
        response = self.client.post(self.login_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class CartAPITests(TestCase):
    """Тесты для API корзины"""
    
    def setUp(self):
        """Настройка перед каждым тестом"""
        self.client = APIClient()
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpassword',
            username='testuser'
        )
        self.client.force_authenticate(user=self.user)
        
        # Создаем корзину для пользователя
        self.cart = Cart.objects.create(user=self.user)
        
        # Создаем тестовый продукт и вариант
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=1000  # в копейках
        )
        
        self.product_variant = ProductVariant.objects.create(
            product=self.product,
            name="Test Variant",
            price=1500,  # в копейках
            stock=10
        )
        
        # Добавляем товар в корзину
        self.cart_item = CartItem.objects.create(
            cart=self.cart,
            product=self.product_variant,
            quantity=2
        )
        
        # URL для API корзины
        self.cart_url = reverse('accounts:cart-detail')
        self.add_to_cart_url = reverse('accounts:add-to-cart')
        self.remove_from_cart_url = reverse('accounts:remove-from-cart')
        
    def test_get_cart(self):
        """Тест получения корзины пользователя"""
        response = self.client.get(self.cart_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['items']), 1)
        self.assertEqual(response.data['items'][0]['product'], self.product_variant.id)
        
    def test_add_to_cart(self):
        """Тест добавления товара в корзину"""
        # Создаем другой вариант продукта
        new_variant = ProductVariant.objects.create(
            product=self.product,
            name="New Variant",
            price=2000,
            stock=5
        )
        
        data = {
            'product_id': new_variant.id,
            'quantity': 3
        }
        
        response = self.client.post(self.add_to_cart_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Проверяем, что товар добавлен в корзину
        cart_items = CartItem.objects.filter(cart=self.cart)
        self.assertEqual(cart_items.count(), 2)
        self.assertTrue(cart_items.filter(product=new_variant).exists())
        
    def test_remove_from_cart(self):
        """Тест удаления товара из корзины"""
        data = {
            'cart_item_id': self.cart_item.id
        }
        
        response = self.client.post(self.remove_from_cart_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Проверяем, что товар удален из корзины
        self.assertEqual(CartItem.objects.filter(cart=self.cart).count(), 0)
