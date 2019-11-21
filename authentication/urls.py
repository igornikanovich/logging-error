from django.urls import path

from .views import RedirectView, registration

urlpatterns = [
    path('', RedirectView.as_view(), name='index'),
    path('register/', registration, name='register'),
]
