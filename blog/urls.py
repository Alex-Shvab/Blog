from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    PostCreateAPIView,
    PostUpdateAPIView,
    PostDeleteAPIView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog_home'),
    path('api_create/', PostCreateAPIView.as_view(), name='api_create'),
    path('api_update/<int:pk>/', PostUpdateAPIView.as_view(), name='api_update'),
    path('api_delete/<int:pk>/', PostDeleteAPIView.as_view(), name='api_delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('about/', views.about, name='blog_about'),
]