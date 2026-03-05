from rest_framework import serializers
from projects.models import TravelProject
from api.v1.places.serializers import PlaceDisplaySerializer


class TravelProjectDisplaySerializer(serializers.ModelSerializer):
    places = PlaceDisplaySerializer(many=True, read_only=True)

    class Meta:
        model = TravelProject
        fields = (
            "id",
            "name",
            "description",
            "start_date",
            "status",
            "places",
        )
