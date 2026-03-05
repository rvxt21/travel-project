from django.urls import path

from api.v1.places import views

urlpatterns = [
    path("create/", views.CreatePlaceAPI.as_view(), name="create-place"),
    path(
        "update/<int:pk>/", views.UpdatePlaceAPI.as_view(), name="update-place"
    ),
]
