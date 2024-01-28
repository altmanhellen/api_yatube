from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import PostViewSet, GroupViewSet, CommentViewSet


api_v1_router = DefaultRouter()
api_v1_router.register(r'posts', PostViewSet, basename='posts')
api_v1_router.register(r'groups', GroupViewSet, basename='groups')
api_v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(api_v1_router.urls)),
]
