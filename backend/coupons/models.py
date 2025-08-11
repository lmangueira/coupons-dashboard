from django.db import models


class Coupon(models.Model):
    """
    Represents a coupon model within the application.

    This class is designed to store and manage coupon information, such as
    discount details, title, associated webshop, and validity periods. It
    supports various types of promotions and can be used to retrieve and
    display coupon-related data.

    :ivar country_code: The originating country code for the coupon.
    :type country_code: str
    :ivar coupon_id: The unique identifier for the coupon.
    :type coupon_id: int
    :ivar coupon_webshop_name: The name of the webshop associated with the
        coupon.
    :type coupon_webshop_name: str
    :ivar description: A detailed description of the coupon.
    :type description: str
    :ivar first_seen: The date the coupon was first seen. Optional field.
    :type first_seen: datetime.date or None
    :ivar last_seen: The date the coupon was last seen. Optional field.
    :type last_seen: datetime.date or None
    :ivar promotion_type: The type of promotion offered by the coupon.
    :type promotion_type: str or None
    :ivar title: The title of the coupon.
    :type title: str
    :ivar value: The value of the discount or offer the coupon provides.
    :type value: int or None
    :ivar webshop_id: The identifier of the webshop associated with the
        coupon.
    :type webshop_id: str
    """

    PROMOTION_TYPE_CHOICES = (
        ("percent-off", "Percent Off"),
        ("buy-one-get-one", "Buy One Get One"),
        ("dollar-off", "Dollar Off"),
        ("free-gift", "Free Gift"),
        ("free-shipping", "Free Shipping"),
    )

    country_code = models.CharField(
        max_length=10, null=False, blank=False, default="us"
    )
    coupon_id = models.IntegerField()
    coupon_webshop_name = models.CharField(
        max_length=255, blank=False, null=False, db_index=True
    )
    description = models.TextField(null=False, blank=False)
    first_seen = models.DateField(null=True, blank=True)
    last_seen = models.DateField(null=True, blank=True)
    promotion_type = models.CharField(
        max_length=50,
        db_index=True,
        choices=PROMOTION_TYPE_CHOICES,
        null=True,
        default=None,
    )
    title = models.CharField(max_length=255, blank=False, null=False)
    value = models.IntegerField(null=True)
    webshop_id = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        if self.promotion_type == "percent-off":
            return f"{self.coupon_webshop_name} - {self.value}% Off: {self.title}"
        return f"{self.coupon_webshop_name} - ${self.value} Off: {self.title}"
