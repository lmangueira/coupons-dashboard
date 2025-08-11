from django.urls import path
from .views import RetailerListView, CouponListView, StatisticsView

urlpatterns = [
    path("retailers/", RetailerListView.as_view(), name="retailer-list"),
    path("statistics/", StatisticsView.as_view(), name="statistics-view"),
    path(
        "statistics/<retailer_name>",
        StatisticsView.as_view(),
        name="statistics-retailer-view",
    ),
    path("coupons/", CouponListView.as_view(), name="coupons-view"),
    path(
        "coupons/<retailer_name>",
        CouponListView.as_view(),
        name="coupons-retailer-view",
    ),
]
