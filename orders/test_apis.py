from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

from orders.models import Order, OrderItem
from products.models import Product, ProductVariant
from accounts.models import Cart, CartItem

User = get_user_model()

class OrderAPITests(TestCase):
    """Тесты для API заказов"""
    
    def setUp(self):
        """Настройка перед каждым тестом"""
        self.client = APIClient()
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpassword',
        )
        self.client.force_authenticate(user=self.user)
        
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
        
        # Создаем заказ
        self.order = Order.objects.create(
            user=self.user,
            status='pending',
            shipping_address='Test Address',
            total_amount=3000  # в копейках
        )
        
        # Добавляем товар в заказ
        self.order_item = OrderItem.objects.create(
            order=self.order,
            product=self.product_variant,
            quantity=2,
            price=1500  # в копейках
        )
        
        # URL для API заказов
        self.orders_url = reverse('orders:order-list')
        self.order_detail_url = reverse('orders:order-detail', args=[self.order.id])
        self.create_order_url = reverse('orders:create-order')
        
    def test_get_orders(self):
        """Тест получения списка заказов пользователя"""
        response = self.client.get(self.orders_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], self.order.id)
        
    def test_get_order_detail(self):
        """Тест получения детальной информации о заказе"""
        response = self.client.get(self.order_detail_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.order.id)
        self.assertEqual(response.data['total_amount'], self.order.total_amount)
        self.assertEqual(len(response.data['items']), 1)
        
    def test_create_order_from_cart(self):
        """Тест создания заказа из корзины"""
        # Создаем корзину для пользователя
        cart = Cart.objects.create(user=self.user)
        
        # Добавляем товар в корзину
        cart_item = CartItem.objects.create(
            cart=cart,
            product=self.product_variant,
            quantity=3
        )
        
        data = {
            'shipping_address': 'New Shipping Address',
            'shipping_method': 'standard'
        }
        
        response = self.client.post(self.create_order_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Проверяем, что заказ создан
        self.assertEqual(Order.objects.count(), 2)
        
        # Проверяем, что корзина очищена
        self.assertEqual(CartItem.objects.filter(cart=cart).count(), 0)
        
    def test_cancel_order(self):
        """Тест отмены заказа"""
        url = reverse('orders:cancel-order', args=[self.order.id])
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Проверяем, что статус заказа изменился
        self.order.refresh_from_db()
        self.assertEqual(self.order.status, 'cancelled')
        
    def test_update_order_status(self):
        """Тест обновления статуса заказа администратором"""
        # Создаем администратора
        admin_user = User.objects.create_user(
            email='admin@example.com',
            password='adminpassword',
            is_staff=True
        )
        
        self.client.force_authenticate(user=admin_user)
        
        url = reverse('orders:update-status', args=[self.order.id])
        data = {
            'status': 'shipped'
        }
        
        response = self.client.patch(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Проверяем, что статус заказа изменился
        self.order.refresh_from_db()
        self.assertEqual(self.order.status, 'shipped')
