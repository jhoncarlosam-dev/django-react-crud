from django.urls import include, path
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from task import views

# Initialize the router
router = routers.DefaultRouter()
router.register(r"task", views.TaskView, basename="task")

# Define task app URLs
urlpatterns = [
    path("api/v1/", include(router.urls)),  # API endpoints
    path("schema/", SpectacularAPIView.as_view(), name="schema"),  # OpenAPI schema
    path("docs/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),  # Swagger UI
    path("docs/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),  # Redoc UI
]
