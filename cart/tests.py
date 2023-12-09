from django.test import TestCase

from cart.models import Cart
from product.models import Product
# Create your tests here.


class CartTest(TestCase):
    def setUp(self):
        product1 = Product.objects.create(title="product 1", price=123123,
                                          discount_price=1231230, count=12, is_active=True)
        product2 = Product.objects.create(title="product 2", price=123123,
                                          discount_price=1231230, count=10, is_active=True)

        Cart.objects.create(product=product1, quantity=10, is_active=True)

        Cart.objects.create(product=product2, quantity=10, is_active=True)

    def test_cart_all_list(self):
        product1 = Product.objects.get(id=1)
        product2 = Product.objects.get(id=1)
        cart1 = Cart.objects.filter(product=product1).first()
        # cart2 = Cart.objects.filter(product=product2).first()

        # self.assertEqual(cart1.update_quantity(), True)
