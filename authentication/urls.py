from django.urls import path, include, reverse_lazy
from django.contrib.auth.views import LogoutView

app_name = 'authentication'

urlpatterns = [
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('blog:homepage')), name="logout"),
]
