from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):

    help = "Creates Facilities"

    def handle(self, *args, **options):
        facilities = ["Free parking on premises", "Gym", "Hot tub", "Pool"]
        for a in facilities:
            Facility.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Facilities created!"))
