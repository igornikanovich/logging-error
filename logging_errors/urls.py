from django.urls import path

from .views import ApplicationListView, ApplicationDetailView

urlpatterns = [
    path('apps/', ApplicationListView.as_view(), name='app_list'),
    path('apps/<int:id>', ApplicationDetailView.as_view(), name='app-detail'),
]
