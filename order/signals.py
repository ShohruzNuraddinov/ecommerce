from django.db.models.signals import pre_save
from django.dispatch import receiver

from order.models import OrderProduct


@receiver(pre_save, sender=OrderProduct)
def update_count(sender, instance, *args, **kwargs):
    is_buy = instance.product.can_buy(instance.quantity)
    if not is_buy:
        return

    print(is_buy)

    if instance.order.status == "INITIAL":
        instance.product.count -= instance.quantity
        instance.product.save()
    elif instance.order.status == "CANCELED":
        instance.product.count += instance.quantity
        instance.product.save()
