from django.urls import path

from api.v1.projects import views

urlpatterns = [
    path("", views.TravelProjectListApi.as_view(), name="project-list"),
]
