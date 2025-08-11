from django.db.models import Count, Min, Max, Avg
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Coupon


class RetailerListView(APIView):
    """
    A view to get a list of unique retailer names (`coupon_webshop_name`).
    """

    def get(self, request, format=None):
        retailers = (
            Coupon.objects.values_list("coupon_webshop_name", flat=True)
            .order_by("coupon_webshop_name")
            .distinct()
        )
        return Response(list(retailers))


class CouponListView(APIView):
    """
    A view to get a list of coupons, whether filtered by retailer name or not.
    """

    def get(self, request, retailer_name=None, format=None):
        qs = Coupon.objects.all().values()
        if retailer_name:
            qs = qs.filter(coupon_webshop_name=retailer_name)

        return Response(qs)


class StatisticsView(APIView):
    """
    A view to return aggregated statistics for coupons.
    It dynamically handles all promotion types found in the data.
    Can be filtered by a retailer: e.g., /api/statistics/Macy's

    Example of the new response structure:
    {
        "retailer": "All",
        "total_coupons": 191,
        "stats_by_type": {
            "percent-off": { "count": 80, "min": "10.00", "max": "75.00", "avg": "25.50" },
            "dollar-off": { "count": 60, "min": "5.00", "max": "50.00", "avg": "12.75" },
            "free-shipping": { "count": 31 },
            "buy-one-get-one": { "count": 15 },
            "free-gift": { "count": 5 }
       }
    }
    """

    def get(self, request, retailer_name=None, format=None):
        """
        Handles the retrieval of coupon statistics by retailer and promotion type.

        :param request: HTTP request object.
        :param retailer_name: Optional; specifies the retailer's name to filter the
            coupons. Defaults to None, meaning all retailers are included.
        :param format: Optional; determines the response format.
        :return: A Response object containing detailed coupon statistics. The structure
            includes the retailer's name (or 'All' if none is specified), the total
            number of coupons, and statistics grouped by promotion type.
        """
        queryset = Coupon.objects.all()
        if retailer_name:
            queryset = queryset.filter(coupon_webshop_name=retailer_name)

        # Get all unique promotion types and their counts
        # This is the most efficient way to get counts for all types in one query.
        type_counts = (
            queryset.values("promotion_type")
            .annotate(count=Count("coupon_id"))
            .order_by("-count")
        )

        # Initialize the main data structure for the response
        stats_by_type = {
            item["promotion_type"]: {"count": item["count"]} for item in type_counts
        }

        # For types with a numeric 'value', calculate detailed stats (min, max, avg)
        # We process these types specifically because they have a meaningful numeric value.
        types_with_value = ["percent-off", "dollar-off"]
        for promo_type in types_with_value:
            # Only run the query if this promo type exists for the selected retailer
            if promo_type in stats_by_type:
                promo_qs = queryset.filter(promotion_type=promo_type)
                detailed_stats = promo_qs.aggregate(
                    min_discount=Min("value"),
                    max_discount=Max("value"),
                    avg_discount=Avg("value"),
                )
                # Update the dictionary for this type with the detailed stats
                stats_by_type[promo_type].update(
                    {
                        "min": f"{detailed_stats['min_discount']:.2f}"
                        if detailed_stats["min_discount"] is not None
                        else "N/A",
                        "max": f"{detailed_stats['max_discount']:.2f}"
                        if detailed_stats["max_discount"] is not None
                        else "N/A",
                        "avg": f"{detailed_stats['avg_discount']:.2f}"
                        if detailed_stats["avg_discount"] is not None
                        else "N/A",
                    }
                )

        # Structure the final response
        response_data = {
            "retailer": retailer_name or "All",
            "total_coupons": queryset.count(),
            "stats_by_type": stats_by_type,
        }

        return Response(response_data)
