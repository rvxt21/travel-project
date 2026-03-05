from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from api.v1.places.serializers import (
    PlaceCreateSerializer,
    PlaceDisplaySerializer,
)


class CreatePlaceAPI(GenericAPIView):
    def post(self, request):
        serializer = PlaceCreateSerializer(data=request.data)

        if serializer.is_valid():
            place = serializer.save()
            return Response(
                PlaceDisplaySerializer(place).data,
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
