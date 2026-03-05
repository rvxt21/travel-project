from django.urls import path

from api.v1.projects import views

urlpatterns = [
    path("", views.TravelProjectListApi.as_view(), name="project-list"),
    path(
        "delete/<int:pk>/",
        views.TravelProjectDeleteAPI.as_view(),
        name="project-delete",
    ),
]
