import os
import tempfile
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

from common.models import MediaFile

User = get_user_model()

class MediaFileAPITests(TestCase):
    """Тесты для API MediaFile"""
    
    def setUp(self):
        """Настройка перед каждым тестом"""
        self.client = APIClient()
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpassword',
            username='testuser'
        )
        self.client.force_authenticate(user=self.user)
        
        # Создаем тестовый файл
        self.media_file = MediaFile.objects.create(
            title="Test Media",
            description="Test Description",
            file="test_file.jpg",
            owner=self.user
        )
        
    def test_get_media_files(self):
        """Проверка получения списка медиафайлов"""
        url = reverse('common:mediafile-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)
        
    def test_create_media_file(self):
        """Проверка создания медиафайла"""
        url = reverse('common:mediafile-create')
        
        # Создаем временный файл для теста
        with tempfile.NamedTemporaryFile(suffix='.jpg') as temp_file:
            temp_file.write(b'test content')
            temp_file.seek(0)
            
            data = {
                'title': 'New Test Media',
                'description': 'New Description',
                'file': temp_file
            }
            
            response = self.client.post(url, data, format='multipart')
            
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MediaFile.objects.count(), 2)
        self.assertEqual(MediaFile.objects.last().title, 'New Test Media')
        
    def test_delete_media_file(self):
        """Проверка удаления медиафайла"""
        url = reverse('common:mediafile-delete', args=[self.media_file.id])
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(MediaFile.objects.count(), 0)
        
    def test_unauthorized_access(self):
        """Проверка доступа неавторизованного пользователя"""
        # Разлогиниваемся
        self.client.force_authenticate(user=None)
        
        # Пытаемся получить список медиафайлов
        url = reverse('common:mediafile-list')
        response = self.client.get(url)
        
        # Ожидаем ответ 401 или 403 в зависимости от настроек DRF
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])
