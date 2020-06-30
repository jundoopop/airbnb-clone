from django.core.management.base import BaseCommand
from rooms.models import RoomType


class Command(BaseCommand):

    help = "Creates roomtypes"

    """     def add_arguments(self, parser):

        parser.add_argument("--times", help="How long will I love you") """

    def handle(self, *args, **options):
        roomtypes = [
            "House",
            "Apartment",
            "Bed and breakfast",
            "Boutique hotel",
            "Bungalow",
            "Cabin",
            "Cottage",
            "Guest suite",
            "Guesthouse",
            "Hostel",
            "Hotel",
            "Loft",
            "Resort",
            "Serviced apartment",
            "Townhouse",
            "Villa",
        ]
        for a in roomtypes:
            RoomType.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("RoomType created!"))
