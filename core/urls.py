from django.urls import path

from core.views import RegistrationView, LoginView, ProfileView

urlpatterns = [
    path('signup', RegistrationView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('profile', ProfileView.as_view(), name='profile'),
]
