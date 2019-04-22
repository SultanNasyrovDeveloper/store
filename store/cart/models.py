from django.db import models
from django.contrib.auth.models import User

from .base import CartBase


class CartItem(models.Model):
    pass


class DatabaseCart(models.Model, CartBase):
    """ Database based cart(Used only with authorized users) """
    @property
    def items_count(self):
        """ Number of items currently in the cart """
        return len(self.cart)

    @property
    def total(self):
        """ Total cart sum """
        return

    def __str__(self):
        """ Cart string representation """
        # TODO implement
        pass

    def add_item(self, item):
        """ Add new item to the cart """
        pass

    def remove_item(self, item):
        """ Remove item from the cart """
        pass

    def clean_cart(self):
        """ Remove all items from the cart """
        pass

    def _save(self):
        """ Save cart to the session """
        self.session = self.cart


