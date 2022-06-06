from rest_framework import generics
from apps.blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, BasePermission, SAFE_METHODS, IsAuthenticatedOrReadOnly


class PostUserWritePermission(BasePermission):
	message = 'Only the creator of a post can edit it.'
	
	def has_object_permission(self, request, view, obj):
		if request.method in SAFE_METHODS:
			return True
		return obj.author == request.user


class PostListView(generics.ListCreateAPIView):
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Post.postobjects.all()
	serializer_class = PostSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
	permission_classes = [PostUserWritePermission]
	queryset = Post.objects.all()
	serializer_class = PostSerializer
