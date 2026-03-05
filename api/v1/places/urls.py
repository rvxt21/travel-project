from django.urls import path

from api.v1.places import views

urlpatterns = [
    path("create/", views.CreatePlaceAPI.as_view(), name="create-place"),
]
