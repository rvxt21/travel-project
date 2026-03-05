from django.db import models


class Place(models.Model):
    project = models.ForeignKey(
        "projects.TravelProject",
        on_delete=models.CASCADE,
        related_name="places",
    )
    name = models.CharField(max_length=250)
    external_id = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(default="", blank=True)
    is_visited = models.BooleanField(default=False)

    def __str__(self):
        return self.name
