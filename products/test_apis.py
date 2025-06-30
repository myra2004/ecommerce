from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

from products.models import Product, ProductVariant, Category, Brand, Size, Color, Review

User = get_user_model()

class ProductAPITests(TestCase):
    """Тесты для API продуктов"""
    
    def setUp(self):
        """Настройка перед каждым тестом"""
        self.client = APIClient()
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpassword',
        )
        self.client.force_authenticate(user=self.user)
        
        # Создаем тестовые категории и бренд
        self.category = Category.objects.create(name="Test Category")
        self.brand = Brand.objects.create(name="Test Brand")
        
        # Создаем тестовый продукт
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=1000,  # в копейках
            brand=self.brand
        )
        self.product.categories.add(self.category)
        
        # Создаем размер и цвет
        self.size = Size.objects.create(name="M")
        self.color = Color.objects.create(name="Red", hex_code="#FF0000")
        
        # Создаем вариант продукта
        self.product_variant = ProductVariant.objects.create(
            product=self.product,
            name="Test Variant",
            price=1500,
            stock=10,
            size=self.size,
            color=self.color
        )
        
        # URL для API продуктов
        self.product_list_url = reverse('products:product-list')
        self.product_detail_url = reverse('products:product-detail', args=[self.product.id])
        
    def test_get_product_list(self):
        """Тест получения списка продуктов"""
        response = self.client.get(self.product_list_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
    def test_get_product_detail(self):
        """Тест получения детальной информации о продукте"""
        response = self.client.get(self.product_detail_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product.name)
        self.assertEqual(response.data['price'], self.product.price)
        
    def test_filter_products_by_category(self):
        """Тест фильтрации продуктов по категории"""
        url = f"{self.product_list_url}?category={self.category.id}"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
    def test_filter_products_by_brand(self):
        """Тест фильтрации продуктов по бренду"""
        url = f"{self.product_list_url}?brand={self.brand.id}"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
    def test_search_products(self):
        """Тест поиска продуктов по названию"""
        url = f"{self.product_list_url}?search=Test"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
        # Поиск, который не должен давать результатов
        url = f"{self.product_list_url}?search=NonExistent"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

class ReviewAPITests(TestCase):
    """Тесты для API отзывов"""
    
    def setUp(self):
        """Настройка перед каждым тестом"""
        self.client = APIClient()
        self.user = User.objects._create_user(
            email='test@example.com',
            password='testpassword',
        )
        self.client.force_authenticate(user=self.user)
        
        # Создаем тестовый продукт
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=1000  # в копейках
        )
        
        # Создаем отзыв
        self.review = Review.objects.create(
            product=self.product,
            user=self.user,
            rating=4,
            text="Great product"
        )
        
        # URL для API отзывов
        self.reviews_url = reverse('products:reviews-list')
        self.review_detail_url = reverse('products:review-detail', args=[self.review.id])
        self.product_reviews_url = reverse('products:product-reviews', args=[self.product.id])
        
    def test_get_reviews(self):
        """Тест получения списка отзывов"""
        response = self.client.get(self.reviews_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
    def test_get_product_reviews(self):
        """Тест получения отзывов для конкретного продукта"""
        response = self.client.get(self.product_reviews_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['product'], self.product.id)
        
    def test_create_review(self):
        """Тест создания отзыва"""
        data = {
            'product': self.product.id,
            'rating': 5,
            'text': 'Excellent product!'
        }
        
        response = self.client.post(self.reviews_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 2)
        
    def test_update_review(self):
        """Тест обновления отзыва"""
        data = {
            'rating': 3,
            'text': 'Updated review text'
        }
        
        response = self.client.patch(self.review_detail_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Проверяем, что отзыв обновлен
        self.review.refresh_from_db()
        self.assertEqual(self.review.rating, 3)
        self.assertEqual(self.review.text, 'Updated review text')
        
    def test_delete_review(self):
        """Тест удаления отзыва"""
        response = self.client.delete(self.review_detail_url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Review.objects.count(), 0)

class CategoryAPITests(TestCase):
    """Тесты для API категорий"""
    
    def setUp(self):
        """Настройка перед каждым тестом"""
        self.client = APIClient()
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpassword',
        )
        self.client.force_authenticate(user=self.user)
        
        # Создаем тестовые категории
        self.category = Category.objects.create(name="Test Category")
        
        # URL для API категорий
        self.categories_url = reverse('products:category-list')
        
    def test_get_categories(self):
        """Тест получения списка категорий"""
        response = self.client.get(self.categories_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.category.name)

class BrandAPITests(TestCase):
    """Тесты для API брендов"""
    
    def setUp(self):
        """Настройка перед каждым тестом"""
        self.client = APIClient()
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpassword',
        )
        self.client.force_authenticate(user=self.user)
        
        # Создаем тестовый бренд
        self.brand = Brand.objects.create(name="Test Brand")
        
        # URL для API брендов
        self.brands_url = reverse('products:brand-list')
        
    def test_get_brands(self):
        """Тест получения списка брендов"""
        response = self.client.get(self.brands_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.brand.name)
