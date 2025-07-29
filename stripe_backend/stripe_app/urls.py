from django.urls import path
from .views import GetCheckoutSessionForItem

urlpatterns = [
    path("get/<int:pk>/", GetCheckoutSessionForItem.as_view()),
]
