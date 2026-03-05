import random
from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from places.models import Place
from projects.models import TravelProject


class Command(BaseCommand):
    help = "Seeds the database with Travel Projects and Places"

    def handle(self, *args, **kwargs):
        self.stdout.write("Cleaning database...")
        Place.objects.all().delete()
        TravelProject.objects.all().delete()

        project_names = [
            "European Capitals",
            "Modern Art",
            "New memories",
            "NEW Project",
            "Good weekends",
        ]

        self.stdout.write("Creating projects...")
        projects_to_create = [
            TravelProject(
                name=name,
                description=lorem_ipsum.paragraph(),
                status=random.choice(["Open", "Completed"]),
            )
            for name in project_names
        ]
        TravelProject.objects.bulk_create(projects_to_create)

        all_projects = TravelProject.objects.all()

        places = [
            {"name": "Paris", "external_id": "	-2147476828"},
            {"name": "London", "external_id": "-2147476055"},
            {"name": "Prague", "external_id": "-2147474881"},
            {"name": "Barcelona", "external_id": "-2147479064"},
            {"name": "Warsaw", "external_id": "-2147481212"},
            {"name": "Berlin", "external_id": "-2147479684"},
            {"name": "Kiev", "external_id": "-2147475677"},
        ]

        self.stdout.write("Populating projects with places...")
        for project in all_projects:
            selected_art = random.sample(places, random.randint(2, 5))

            for art in selected_art:
                Place.objects.create(
                    project=project,
                    name=art["name"],
                    external_id=art["external_id"],
                    notes=f"Note: {lorem_ipsum.sentence()}",
                    is_visited=random.choice([True, False]),
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully seeded {all_projects.count()} projects!"
            )
        )
