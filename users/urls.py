from django.urls import path

from users.views import UserLoginView, UserLogoutView, UserRegistrationView


urlpatterns = [
    path('users/login/', UserLoginView.as_view(), name='user-login'),
    path('users/logout/', UserLogoutView.as_view(), name='user-logout'),
    path('users/registration/', UserRegistrationView.as_view(), name='user-registration'),
]