from ..models import Item
from django.core.exceptions import ObjectDoesNotExist


class ItemService:
    """
    Класс для сервисной логики Item
    """

    @classmethod
    def get_object_by_pk(cls, pk: int):
        """
        Получаем объект Item по его
        Primary Key
        """
        item = Item.objects.get(id=pk)
        return item
