import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View

stripe.api_key = settings.STRIPE_SECRET_KEY
DOMAIN = settings.DOMAIN


class StripeAPI(View):
    """
    Класс для работы с API Stripe.
    """

    def post(self, item):
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": item.name,
                        },
                        "unit_amount": item.price,
                    },
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url=DOMAIN + "/success/",
            cancel_url=DOMAIN + "/cancel/",
        )
        return JsonResponse({"id": checkout_session.id})
