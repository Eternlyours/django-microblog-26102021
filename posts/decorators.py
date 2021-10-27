from functools import wraps

from django.http import HttpResponseRedirect
from django.urls.base import reverse_lazy

from posts.models import Post


def author_verification(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if request.user != Post.objects.get(slug=kwargs['slug']).author:
            return HttpResponseRedirect(reverse_lazy('post-list'))
        return function(request, *args, **kwargs)
    return wrap
