from django.urls import reverse
from rest_framework.test import APITestCase
from apps.blog.models import Category, Post
from apps.user.models import MyUser


class TestPost(APITestCase):
	data = {
		'title': 'new',
		'author': 1,
		'excerpt': 'new',
		'content': 'new'
	}
	
	@classmethod
	def setUpTestData(cls):
		cls.test_category = Category.objects.create(name='django')
		cls.test_user_1 = MyUser.objects.create_user(username='test_user_1', password='password123')
	
	def test_get(self):
		url = reverse('blog_api:list_create')
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, 200)
	
	def test_post_create(self):
		url = reverse('blog_api:list_create')
		self.client.force_login(self.test_user_1)
		
		self.assertEqual(len(Post.objects.all()), 0)
		response = self.client.post(url, self.data, format='json')
		self.assertEqual(response.status_code, 201)
		self.assertEqual(len(Post.objects.all()), 1)
	
	def test_post_update(self):
		Post.objects.create(
			category_id=1,
			author_id=1,
			title='Original',
			excerpt='Original',
			content='Original',
			status='published'
		)
		url = reverse('blog_api:detail_create', args=[1])
		self.client.force_login(self.test_user_1)
		response = self.client.put(
			url, {
				'title': 'New',
				'author': 1,
				'excerpt': 'New',
				'content': 'New',
				'status': 'published'
			}, format='json')
		self.assertEqual(response.status_code, 200)
		
		updated = Post.objects.get(id=1)
		self.assertEqual(updated.title, 'New')
		self.assertEqual(updated.excerpt, 'New')
		self.assertEqual(updated.content, 'New')
		