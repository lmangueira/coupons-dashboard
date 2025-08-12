from django.core.management.base import BaseCommand
from django.conf import settings

from coupons.models import Coupon


class Command(BaseCommand):
    help = "Checks how many coupons are in DB. Needed for shell checks"

    def handle(self, *args, **options):
        try:
            self.stdout.write(f"{Coupon.objects.count()}")

        except Exception as e:
            self.style.ERROR(f"Error while checking coupons in DB: {e}")
            return
