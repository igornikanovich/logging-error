from django.urls import path

from .views import ErrorCreateView


urlpatterns = [
    path('crash/<token>/', ErrorCreateView.as_view()),
]

