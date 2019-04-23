from django.db import models
from django.contrib.auth.models import User

from .base import CartBase


class DatabaseCart(models.Model, CartBase):
    """ Database based cart(Used only with authorized users) """

    @property
    def items_count(self):
        """ Number of items currently in the cart """
        return

    @property
    def total(self):
        """ Total cart sum """
        return

    def __str__(self):
        """ Cart string representation """
        pass

    def add_item(self, item):
        """ Add new item to the cart """
        pass

    def delete_item(self, item):
        """ Remove item from the cart """
        pass

    def clean_cart(self):
        """ Remove all items from the cart """
        pass


class CartItem(models.Model):
    """ Cart item model for database cart """
    cart = models.ForeignKey(DatabaseCart, on_delete=models.CASCADE, related_name='items', related_query_name='items')
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=1, verbose_name='Quantity')


class Order(models.Model):
    pass


class OrderItem(models.Model):
    pass






