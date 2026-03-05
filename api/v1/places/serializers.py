from rest_framework import serializers
from places.models import Place


class PlaceDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = (
            "id",
            "name",
            "external_id",
            "notes",
            "is_visited",
        )
