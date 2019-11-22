from django.urls import path

from .views import RedirectView, UserRegistrationView

urlpatterns = [
    path('', RedirectView.as_view(), name='index'),
    path('register/', UserRegistrationView.as_view(), name='register'),
]
