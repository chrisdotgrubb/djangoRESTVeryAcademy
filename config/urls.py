from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('apps.blog.urls', namespace='blog')),
	path('api/', include('apps.blog_api.urls', namespace='blog_api')),
	path('api/user/', include('apps.user.urls', namespace='user')),
	path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
