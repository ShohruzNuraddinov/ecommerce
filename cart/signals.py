from django.db.models.signals import pre_save
from django.dispatch import receiver

from cart.models import Cart
from order.models import Order


# @receiver(pre_save, sender=Cart)
# def update_quantity(sender, instance, *args, **kwargs):
#     print(instance)
#     if instance.update_quantity:
#         total_price = instance.product.price * instance.quantity
#         total_discount = instance.product.discount_price * instance.quantity
#         Order.objects.create(
#             user=instance.user, total_price=total_price, total_discount=total_discount)
