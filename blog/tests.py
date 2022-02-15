from django.test import TestCase

# Create your tests here.

from .models import Post
from authentication.models import User
from datetime import date

from django.conf import settings
from django.urls import reverse

"""
class PostModelTests(TestCase):
    def setUp(self):
        Post.objects.create(title="This is an article", content="this is content")
        Post.objects.create(title="new article title", content="interesting content")

    def test_create_model(self):
        post = Post(title="this is an article", content="this is content", snippet="hello")
        self.assertEqual(post.title, "this is an article")
        self.assertEqual(post.content, "interesting content")
        self.assertEqual(post.snippet, "hello")

    def test_date_created(self):
        post = Post.objects.get(pk=1)
        self.assertEqual(post.created_on.date(), date.today())
"""


class HomepageViewTests(TestCase):
    def setUp(self):
        user = User.objects.create(email="darko.dekan@gmail.com", password="hello123", username="hello")
        Post.objects.create(title="This is an article", content="this is content", author=user, slug="this-is-ab-article")
        Post.objects.create(title="new article title", content="interesting content", author=user, slug="this-is-not")
        Post.objects.create(title="some other", content="interesting content", author=user, slug="this-is-there")

    def test_request(self):
        response = self.client.get(reverse("blog:homepage"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"This is an article", response.content)


class PostListViewTests(TestCase):
    def test_request(self):
        response = self.client.get(reverse("blog:post_list"))
        self.assertEqual(response.status_code, 200)


