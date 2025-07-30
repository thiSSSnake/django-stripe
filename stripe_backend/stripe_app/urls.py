from django.urls import path
from .views import (
    GetCheckoutSessionForItem,
    ItemView,
    ItemsListView,
    SuccessView,
    CancelView,
)

urlpatterns = [
    path("", ItemsListView.as_view(), name="main-page"),
    path(
        "buy/<int:pk>",
        GetCheckoutSessionForItem.as_view(),
        name="create-checkout-session",
    ),
    path("item/<int:pk>", ItemView.as_view(), name="get-item-info"),
    path("cancel/", CancelView.as_view()),
    path("success/", SuccessView.as_view()),
]
