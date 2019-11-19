from django.urls import path

from .views import ApplicationListView, ApplicationDetailView

urlpatterns = [
    path('app/', ApplicationListView.as_view(), name='app_list'),
    path('app/<int:id>', ApplicationDetailView.as_view(), name='app-detail'),
]
