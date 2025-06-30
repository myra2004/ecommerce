from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

from payments.models import Transaction
from orders.models import Order

User = get_user_model()

class TransactionAPITests(TestCase):
    """Тесты для API транзакций"""
    
    def setUp(self):
        """Настройка перед каждым тестом"""
        self.client = APIClient()
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpassword',
        )
        self.client.force_authenticate(user=self.user)
        
        # Создаем заказ
        self.order = Order.objects.create(
            user=self.user,
            status='pending',
            shipping_address='Test Address',
            total_amount=3000  # в копейках
        )
        
        # Создаем транзакцию
        self.transaction = Transaction.objects.create(
            user=self.user,
            order=self.order,
            amount=3000,  # в копейках
            status='pending',
            payment_method='card'
        )
        
        # URL для API транзакций
        self.transactions_url = reverse('payments:transaction-list')
        self.transaction_detail_url = reverse('payments:transaction-detail', args=[self.transaction.id])
        self.process_payment_url = reverse('payments:process-payment')
        
    def test_get_transactions(self):
        """Тест получения списка транзакций пользователя"""
        response = self.client.get(self.transactions_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], self.transaction.id)
        
    def test_get_transaction_detail(self):
        """Тест получения детальной информации о транзакции"""
        response = self.client.get(self.transaction_detail_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.transaction.id)
        self.assertEqual(response.data['amount'], self.transaction.amount)
        
    def test_process_payment(self):
        """Тест обработки платежа"""
        data = {
            'order_id': self.order.id,
            'payment_method': 'card',
            'card_number': '4111111111111111',
            'expiry_date': '12/24',
            'cvv': '123'
        }
        
        response = self.client.post(self.process_payment_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Проверяем, что статус транзакции изменился
        self.transaction.refresh_from_db()
        self.assertEqual(self.transaction.status, 'completed')
        
        # Проверяем, что статус заказа также изменился
        self.order.refresh_from_db()
        self.assertEqual(self.order.status, 'paid')
        
    def test_refund_payment(self):
        """Тест возврата платежа"""
        # Сначала устанавливаем статус транзакции как completed
        self.transaction.status = 'completed'
        self.transaction.save()
        
        url = reverse('payments:refund-payment', args=[self.transaction.id])
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Проверяем, что статус транзакции изменился
        self.transaction.refresh_from_db()
        self.assertEqual(self.transaction.status, 'refunded')
