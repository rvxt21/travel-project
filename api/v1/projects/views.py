from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.request import Request
from api.v1.projects.serializers import (
    TravelProjectDisplaySerializer,
    TravelProjectUpdateSerializer,
)
from projects.models import TravelProject


class TravelProjectListApi(ListAPIView):
    queryset = TravelProject.objects.all()
    serializer_class = TravelProjectDisplaySerializer


class TravelProjectDeleteAPI(GenericAPIView):
    def delete(self, request: Request, pk: int):
        project = get_object_or_404(TravelProject, pk=pk)

        if project.places.filter(is_visited=True).exists():
            return Response(
                {
                    "error": "This project cannot be deleted because it contains visited places."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        project.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class TravelProjectUpdateAPI(GenericAPIView):
    def patch(self, request: Request, pk: int) -> Response:
        project = get_object_or_404(TravelProject, pk=pk)

        serializer = TravelProjectUpdateSerializer(
            instance=project, data=request.data, partial=True
        )

        if serializer.is_valid():
            project = serializer.save()
            return Response(
                TravelProjectDisplaySerializer(project).data,
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
