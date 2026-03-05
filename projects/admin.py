from django.contrib import admin
from projects.models import TravelProject
from places.models import Place


class TravelPlaceTabular(admin.TabularInline):
    model = Place
    extra = 0


class TravelProjectAdmin(admin.ModelAdmin):
    inlines = [
        TravelPlaceTabular,
    ]
    list_display = ["name", "description", "start_date", "status"]


admin.site.register(TravelProject, TravelProjectAdmin)
