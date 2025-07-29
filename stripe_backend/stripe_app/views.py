from django.views import View
from django.views.generic import TemplateView
from django.http import JsonResponse
from .services.item_service import ItemService
from .stripe_api.controller import StripeAPI
from .models import Item
from django.core.exceptions import ObjectDoesNotExist


class GetCheckoutSessionForItem(View):

    def get_item(self, request, *args, **kwargs):
        """
        Метод для получения объекта Item
        по ключу Primary Key
        """
        pk = self.kwargs["pk"]
        item = ItemService.get_object_by_pk(pk=pk)
        return item

    def get_session_id_for_item(self, item):
        """
        Метод для получения id сессии Stripe
        """
        stripe_session = StripeAPI()
        stripe_session_id = stripe_session.post(item=item)
        return stripe_session_id

    def get(self, request, *args, **kwargs):
        """
        Метод GET
        для получения id сессии Stripe
        для конкретного объекта Item
        """
        try:
            item = self.get_item(request)
            session_id = self.get_session_id_for_item(item=item)
            return session_id
        except ObjectDoesNotExist:
            return JsonResponse({"error": "Error while fetching item"})


class ItemView(TemplateView):
    template_name = "item/checkout.html"

    def get_context_data(self, **kwargs):
        item = ItemService.get_object_by_pk(self.kwargs["pk"])

        context = super(ItemView, self).get_context_data(**kwargs)
        context.update({"item": item})
        return context
