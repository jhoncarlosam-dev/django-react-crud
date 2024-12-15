from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),  # Admin panel
    path("task/", include("task.urls")),  # Delegate to task app's URLs
]
