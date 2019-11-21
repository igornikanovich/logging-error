from django.urls import path

from .views import ApplicationListView, ErrorApplicationListView

urlpatterns = [
    path('', ApplicationListView.as_view(), name='app_list'),
    path('<int:id>/', ErrorApplicationListView.as_view(), name='app-detail'),
]
