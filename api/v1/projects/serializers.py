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


class TravelProjectUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False, allow_blank=True)
    start_date = serializers.DateField(required=False)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.start_date = validated_data.get(
            "start_date", instance.start_date
        )

        instance.save()
        return instance


class TravelProjectPlacesDisplaySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    places = PlaceDisplaySerializer(many=True, read_only=True)
