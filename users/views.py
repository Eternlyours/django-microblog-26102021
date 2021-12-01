from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls.base import reverse_lazy

from users.forms import UserCreationCustomForm


class UserRegistrationView(CreateView):
    template_name = 'registration.html'
    form_class = UserCreationCustomForm
    success_url = reverse_lazy('post-list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class UserLoginView(LoginView):
    template_name = 'login.html'
    
    def get_success_url(self):
        url = self.get_redirect_url()
        return url or reverse_lazy('post-list')


class UserLogoutView(LogoutView):
    template_name = 'logout.html'
    
