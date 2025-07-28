from decimal import Decimal
from django.db import models


class Item(models.Model):
    name = models.CharField(
        verbose_name="Наименование",
        max_length=250,
    )
    description = models.TextField(verbose_name="Описание", blank=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal("0.00"),
        verbose_name="Цена",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return f"{self.name} - {self.price}"
