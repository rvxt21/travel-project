from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from places.models import Place
from api.v1.places.serializers import (
    PlaceCreateSerializer,
    PlaceDisplaySerializer,
    PlaceUpdateSerializer,
)


class CreatePlaceAPI(GenericAPIView):
    def post(self, request: Request) -> Response:
        serializer = PlaceCreateSerializer(data=request.data)

        if serializer.is_valid():
            place = serializer.save()
            return Response(
                PlaceDisplaySerializer(place).data,
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdatePlaceAPI(GenericAPIView):
    def patch(self, request: Request, pk: int) -> Response:
        place = get_object_or_404(Place, pk=pk)

        serializer = PlaceUpdateSerializer(
            instance=place, data=request.data, partial=True
        )

        if serializer.is_valid():
            place = serializer.save()

            return Response(
                PlaceDisplaySerializer(place).data, status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
