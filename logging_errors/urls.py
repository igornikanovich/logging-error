from django.urls import path

from .views import ApplicationListView, ErrorDetailView, ErrorListView, ApplicationDetailView

urlpatterns = [
    path('', ApplicationListView.as_view(), name='app_list'),
    path('app/<int:id>', ApplicationDetailView.as_view(), name='app-detail'),
    path('errors/', ErrorListView.as_view(), name='errors_list'),
    path('errors/<int:id>', ErrorDetailView.as_view(), name='error-detail'),
]