import json

from django.core.management.base import BaseCommand
from django.conf import settings

from coupons.models import Coupon


class Command(BaseCommand):
    help = "Seeds the database from a coupons.json file in the project root"

    def handle(self, *args, **options):
        self.stdout.write("Deleting old coupon data...")
        Coupon.objects.all().delete()
        json_file_path = settings.BASE_DIR / "coupons.json"
        try:
            with open(json_file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            self.stdout.write(
                self.style.ERROR(
                    f"Error: `coupons.json` not found in the project root directory."
                )
            )
            return
        except json.JSONDecodeError:
            self.stdout.write(
                self.style.ERROR(
                    f"Error: Could not decode JSON. Please check the format of `coupons.json`."
                )
            )
            return
        self.stdout.write("Loading new coupon data from JSON file...")
        coupons_to_create = []
        for item in data.get("coupons", []):
            coupons_to_create.append(
                Coupon(
                    country_code=item.get("country_code"),
                    coupon_id=item.get("coupon_id"),
                    coupon_webshop_name=item.get("coupon_webshop_name"),
                    description=item.get("description"),
                    first_seen=item.get("first_seen"),
                    last_seen=item.get("last_seen"),
                    promotion_type=item.get("promotion_type"),
                    title=item.get("title"),
                    value=item.get("value"),
                    webshop_id=item.get("webshop_id"),
                )
            )
        if coupons_to_create:
            Coupon.objects.bulk_create(coupons_to_create)
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully seeded the database with {len(coupons_to_create)} coupons."
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING("No coupons found in the JSON file to seed.")
            )
