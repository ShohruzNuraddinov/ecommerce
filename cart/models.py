from django.db import models
from django.contrib.auth.models import User

from product.models import Product
from order.models import Order

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='carts')
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def update_quantity(self):
        if self.product.count < self.quantity:
            return False
        return True

    def save(self, *args, **kwargs):
        if not self.update_quantity:
            return ValueError('value is not enough')

        return super().save(*args, **kwargs)
