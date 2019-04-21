from django.contrib.auth.models import User


class CartBase(object):

    @property
    def total(self):
        return NotImplementedError

    @property
    def items_number(self):
        return NotImplementedError

    @property
    def items_list(self):
        return NotImplementedError

    def add_item(self):
        return NotImplementedError

    def remove_item(self):
        return NotImplementedError

    def change_quantity(self):
        return NotImplementedError


class SessionCart(CartBase):
    pass


def simple_cart_factory(user):
    # TODO implement
    # if user authenticated
    # return DatabaseCart
    # else
    # return session cart
    pass
