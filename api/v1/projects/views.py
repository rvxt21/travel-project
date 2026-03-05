from rest_framework import status
from rest_framework.generics import ListAPIView
from api.v1.projects.serializers import TravelProjectDisplaySerializer
from projects.models import TravelProject


class TravelProjectListApi(ListAPIView):
    queryset = TravelProject.objects.all()
    serializer_class = TravelProjectDisplaySerializer
