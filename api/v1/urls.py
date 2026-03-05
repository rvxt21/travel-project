from django.urls import path, include


urlpatterns = [
    path("projects/", include("api.v1.projects.urls")),
    path("places/", include("api.v1.places.urls")),
]
