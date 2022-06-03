from django.urls import reverse
from rest_framework.test import APITestCase
from apps.blog.models import Category, Post
from apps.user.models import MyUser


class TestPost(APITestCase):
	
	def test_view_post(self):
		url = reverse('blog_api:list_create')
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, 200)

	def test_create_post(self):
		self.test_category = Category.objects.create(name='django')
		self.test_user_1 = MyUser.objects.create_user(username='test_user_1', password='password123')
		data = {
			'title': 'new',
			'author': 1,
			'excerpt': 'new',
			'content': 'new'
		}
		url = reverse('blog_api:list_create')
		
		self.assertEqual(len(Post.objects.all()), 0)
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, 201)
		self.assertEqual(len(Post.objects.all()), 1)
		