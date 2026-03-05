from django.contrib import admin
from places.models import Place


class PlaceAdmin(admin.ModelAdmin):
    list_display = ["project", "name", "notes", "is_visited"]
    raw_id_fields = ["project"]


admin.site.register(Place, PlaceAdmin)
