from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('logging_errors.urls')),
    path('api/', include('logging_errors.api.v1.urls')),
]
