from django.db import models
from django.contrib.auth.models import User

# from product.models import Product

# Create your models here.


class OrderStatusChoices(models.TextChoices):
    INITIAL = 'INITIAL'
    PAYMENT = 'PAYMENT'
    ACCEPTED = 'ACCEPTED'
    CANCELED = 'CANCELED'
    DELIVERED = 'DELIVERED'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    total_price = models.IntegerField()
    total_discount = models.IntegerField()

    status = models.CharField(max_length=255, choices=OrderStatusChoices.choices, default=OrderStatusChoices.INITIAL)  # noqa


class OrderProduct(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order_product')
    product = models.ForeignKey(
        'product.Product', on_delete=models.CASCADE, related_name='orders')
    price = models.IntegerField()
    quantity = models.IntegerField()
