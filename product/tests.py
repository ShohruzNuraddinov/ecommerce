from django.test import TestCase

from product.models import Product
# Create your tests here.


class ProductTest(TestCase):
    def setUp(self):
        Product.objects.create(title="product 1", price=123123,
                               discount_price=1231230, count=12, is_active=True)
        Product.objects.create(title="product 2", price=123123123,
                               discount_price=1231231230, count=10, is_active=True)
        # print(1)
