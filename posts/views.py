from django.contrib.auth.decorators import login_required
from django.http.response import Http404, HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .decorators import author_verification
from posts.forms import PostForm
from posts.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'post-list.html'

    def get_queryset(self):
        return super().get_queryset().select_related('author')


class PostDetailView(DetailView):
    model = Post
    template_name = 'post-detail.html'

    def get_queryset(self):
        return super().get_queryset().select_related('author')


class PostCreateView(CreateView):
    model = Post
    template_name = 'post-create.html'
    form_class = PostForm

    @method_decorator(login_required(login_url=reverse_lazy('post-list')))
    def post(self, request, *args: str, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post-update.html'
    form_class = PostForm

    def get_queryset(self):
        return super().get_queryset().select_related('author')

    @method_decorator(login_required)
    @method_decorator(author_verification)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @method_decorator(login_required)
    @method_decorator(author_verification)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
