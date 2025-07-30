from ..models import Item
from django.core.exceptions import ObjectDoesNotExist


# В будущем можно использовать этот класс для
# модульного тестирования логики работы с Item
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

    @classmethod
    def get_all_objects(cls):
        """
        Получаем все объекты
        """
        items = Item.objects.all()
        return items
