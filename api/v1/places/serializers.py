from rest_framework import serializers
from places.models import Place
from projects.models import TravelProject
from places.services.validators import validate_place_via_artic_api


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


class PlaceCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    notes = serializers.CharField(required=False, allow_blank=True, default="")
    project = serializers.PrimaryKeyRelatedField(
        queryset=TravelProject.objects.all()
    )

    def validate(self, data):
        project = data.get("project")
        place_name = data.get("name")

        if project.places.count() >= 10:
            raise serializers.ValidationError(
                "This project already has the maximum of 10 places."
            )

        external_id = validate_place_via_artic_api(place_name)

        if external_id is None:
            raise serializers.ValidationError(
                f"Place '{place_name}' could not be validated with the Art Institute API."
            )

        if project.places.filter(external_id=external_id).exists():
            raise serializers.ValidationError(
                "This place is already in your project."
            )

        data["external_id"] = external_id
        return data

    def create(self, validated_data):

        return Place.objects.create(**validated_data)


class PlaceUpdateSerializer(serializers.Serializer):
    notes = serializers.CharField(required=False, allow_blank=True)
    is_visited = serializers.BooleanField(required=False)

    def update(self, instance, validated_data):
        instance.notes = validated_data.get("notes", instance.notes)
        instance.is_visited = validated_data.get(
            "is_visited", instance.is_visited
        )

        instance.save()
        return instance
