from django.db import models


class TravelProject(models.Model):
    class StatusChoice(models.TextChoices):
        OPEN = "Open"
        COMPLETED = "Completed"

    name = models.CharField(max_length=250)
    description = models.TextField(default="", blank=True)
    start_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=15, choices=StatusChoice.choices, default=StatusChoice.OPEN
    )
