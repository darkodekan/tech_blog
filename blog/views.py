from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Post
from .forms import PostSearchForm
from django.db.models import Q

# Create your views here.


class HomepageView(TemplateView):
    template_name = "blog/home.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['featured_posts'] = Post.objects.all().order_by('-id')[:4]
        return context


class Error404(TemplateView):
    template_name = "blog/404.html"


class PostListView(ListView):
    paginate_by = 10
    model = Post
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = PostSearchForm(self.request.GET)
        return context

    def get_queryset(self):
        form = PostSearchForm(self.request.GET)
        if form.is_valid():
            query = Q(title__icontains=form.cleaned_data['query'])
            return Post.objects.filter(query)
        return Post.objects.all()


class PostDetailView(DetailView):
    model = Post

"""
class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post


class PostUpdateView(UpdateView, LoginRequiredMixin):
    model = Post


class PostDeleteView(DeleteView):
    model = Post
"""
