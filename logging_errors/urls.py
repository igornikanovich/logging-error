from django.urls import path

from .views import ApplicationListView, ErrorApplicationListView

urlpatterns = [
    path('apps/', ApplicationListView.as_view(), name='app_list'),
    path('apps/<int:id>', ErrorApplicationListView.as_view(), name='app-detail'),
]
