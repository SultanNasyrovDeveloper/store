from django.db import models
from django.contrib.auth.models import User

from store.catalog.models import Product


class WishList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    products = models.ManyToManyField('catalog.Product', blank=True, verbose_name='Products')

    class Meta:
        verbose_name = 'wish list'
        verbose_name_plural = 'wish lists'

    def __str__(self):
        return 'Wish List {}, user {}'.format(self.id, self.user.username)

    def add_product(self, product_id):
        """ Add product to wish list by id """
        product = Product.objects.get(id=product_id)
        self.products.add(product)
        self.save()

    def delete_product(self, product_id):
        """ Delete product from wish list by id """
        product = Product.objects.get(id=product_id)
        self.products.remove(product)
        self.save()

    def product_to_cart(self):
        # TODO Implement when cart is ready
        pass

