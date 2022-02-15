from django.urls import path, include
from .views import HomepageView, PostListView, PostDetailView

app_name = 'blog'

urlpatterns = [
    path('', HomepageView.as_view(), name="homepage"),
    path('posts/', PostListView.as_view(), name="post_list"),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name="post_detail")
]
