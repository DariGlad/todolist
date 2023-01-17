from django.urls import path

from core.views import RegistrationView

urlpatterns = [
    path('signup', RegistrationView.as_view(), name='signup')
]