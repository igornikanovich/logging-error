from django.urls import path

from .views import ApplicationListView, ErrorListView

urlpatterns = [
    path('', ApplicationListView.as_view(), name='app_list'),
    path('test/', ErrorListView.as_view(), name='test'),
]