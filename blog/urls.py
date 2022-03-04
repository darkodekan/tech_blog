from django.urls import path, include
from .views import PostListView, PostDetailView, PostCreateView
from django.shortcuts import redirect

app_name = 'blog'

urlpatterns = [
    path('', lambda req: redirect('blog:post_list')),
    path('posts/', PostListView.as_view(), name="post_list"),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name="post_detail"),
    path('add-post/', PostCreateView.as_view(), name="post_form"),

]
