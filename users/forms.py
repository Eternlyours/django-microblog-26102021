from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


class UserCreationCustomForm(UserCreationForm):
    remember_me = forms.BooleanField(required=False, label='Запомнить меня')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super().save(commit=commit)
        if self.cleaned_data['remember_me']:
            login(self.request, user)
        return user