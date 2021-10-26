from django.urls import path

from posts.views import PostCreateView, PostDetailView, PostListView, PostUpdateView


urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/create/', PostCreateView.as_view(), name='post-create'),
    path('posts/update/<slug:slug>', PostUpdateView.as_view(), name='post-update'),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
]