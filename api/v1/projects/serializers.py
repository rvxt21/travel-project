from rest_framework import serializers
from projects.models import TravelProject


class TravelProjectDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelProject
        fields = (
            "id",
            "name",
            "description",
            "start_date",
            "status",
        )
