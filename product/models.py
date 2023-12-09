from collections.abc import Iterable
from django.db import models

from order.models import OrderProduct
# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    discount_price = models.IntegerField()
    count = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def active(self):
        if self.count < 0 and not self.is_active:
            return False
        return True

    def can_buy(self, quantity):
        all_product = Product.objects.filter(product=self).aggregate(total_quantity=models.Sum('count'))  # noqa
        holded_produtcs = OrderProduct.objects.filter(product=self).filter(models.Q(
            order__status="INITIAL") | models.Q(order__status="PAYMENT")).aggregate(total_quantity=models.Sum('quantity'))  # noqa
        return all_product['total_quantity'] - holded_produtcs['total_quantity'] > quantity and self.active()
