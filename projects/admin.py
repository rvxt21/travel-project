from django.contrib import admin
from projects.models import TravelProject


class TravelProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "start_date", "status"]


admin.site.register(TravelProject, TravelProjectAdmin)
