from django.urls import path
from .views import PostListView, PostDetailView
app_name = 'blog_api'

urlpatterns = [
	path('', PostListView.as_view(), name='list_create'),
	path('<int:pk>/', PostDetailView.as_view(), name='detail_create'),
	
]
