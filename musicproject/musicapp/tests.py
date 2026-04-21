from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import CustomUser
from .models import MusicPost, Category

class MusicAppTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password123'
        )
        self.category = Category.objects.create(title='Rock')
        self.post = MusicPost.objects.create(
            user=self.user,
            title='Test Song',
            content='Test Content'
        )

    def test_index_view(self):
        """トップページが正常に表示されるかテスト"""
        response = self.client.get(reverse('musicapp:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Song')

    def test_search_functionality(self):
        """検索機能が正常にフィルタリングされるかテスト"""
        response = self.client.get(reverse('musicapp:index'), {'search': 'Test'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Song')

        response = self.client.get(reverse('musicapp:index'), {'search': 'Nonexistent'})
        self.assertNotContains(response, 'Test Song')

    def test_post_detail_view(self):
        """詳細ページが正常に表示されるかテスト"""
        response = self.client.get(reverse('musicapp:photo_detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Song')
