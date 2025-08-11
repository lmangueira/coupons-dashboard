from django.contrib import admin
from .models import Coupon


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = (
        "coupon_id",
        "coupon_webshop_name",
        "title",
        "promotion_type",
        "value",
        "country_code",
        "first_seen",
        "last_seen",
        "webshop_id",
    )
    list_filter = (
        "promotion_type",
        "country_code",
        "first_seen",
        "last_seen",
    )
    search_fields = (
        "coupon_webshop_name",
        "title",
        "description",
        "webshop_id",
    )
    ordering = ("-last_seen", "coupon_id")
    list_per_page = 50
