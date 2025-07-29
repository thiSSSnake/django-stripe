from django.views import View
from django.http import JsonResponse
from .services.item_service import ItemService
from .stripe_api.controller import StripeAPI
from .models import Item


class GetCheckoutSessionForItem(View):

    def get_item(self, request, *args, **kwargs):
        pk = self.kwargs["pk"]
        item = ItemService.get_object_by_pk(pk=pk)
        return item

    def get_session_id_for_item(self, item):
        stripe_session = StripeAPI()
        stripe_session_id = stripe_session.post(item=item)
        return stripe_session_id

    def get(self, request, *args, **kwargs):
        item = self.get_item(request)
        session_id = self.get_session_id_for_item(item=item)
        return session_id
