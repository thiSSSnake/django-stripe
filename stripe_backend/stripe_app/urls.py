from django.urls import path
from .views import GetCheckoutSessionForItem, ItemView

urlpatterns = [
    path(
        "get/buy/<int:pk>",
        GetCheckoutSessionForItem.as_view(),
        name="get-checkout-session",
    ),
    path("get/item/<int:pk>", ItemView.as_view(), name="get-item-info"),
]
