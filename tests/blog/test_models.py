from django.test import TestCase
from apps.blog.models import Post, Category
from apps.user.models import MyUser


class TestCategory(TestCase):
	name = 'Test Category Name'
	
	@classmethod
	def setUpTestData(cls):
		cls.test_category = Category.objects.create(name=cls.name)

	def test_category_content(self):
		self.assertEqual(self.test_category.name, self.name)
		
	def test_str(self):
		self.assertEqual(str(self.test_category), self.name)
	
	
class TestPost(TestCase):
	title = 'Post Title'
	excerpt = 'Post Excerpt'
	content = 'Post Content'
	slug = 'post-title'
	status = 'published'
	
	@classmethod
	def setUpTestData(cls):
		Category.objects.create(name='django')
		cls.test_user_1 = MyUser.objects.create_user(username='test_user_1', password='password123')
		cls.test_post = Post.objects.create(
			category_id=1,
			title=cls.title,
			excerpt=cls.excerpt,
			content=cls.content,
			slug=cls.slug,
			author_id=1,
			status=cls.status
		)
	
	def test_post_content(self):
		post = Post.postobjects.get(id=1)
		author = post.author
		excerpt = f'{post.excerpt}'
		title = f'{post.title}'
		content = f'{post.content}'
		slug = f'{post.slug}'
		status = f'{post.status}'
		self.assertEqual(author, self.test_user_1)
		self.assertEqual(title, self.title)
		self.assertEqual(excerpt, self.excerpt)
		self.assertEqual(content, self.content)
		self.assertEqual(slug, self.slug)
		self.assertEqual(status, self.status)
	
	def test_str(self):
		self.assertEqual(str(self.test_post), self.title)
