from django.urls import path
from .views import GetCheckoutSessionForItem, ItemView, SuccessView, CancelView

urlpatterns = [
    path(
        "buy/<int:pk>",
        GetCheckoutSessionForItem.as_view(),
        name="create-checkout-session",
    ),
    path("item/<int:pk>", ItemView.as_view(), name="get-item-info"),
    path("cancel/", CancelView.as_view()),
    path("success/", SuccessView.as_view()),
]
