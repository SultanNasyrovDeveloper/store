from .base import CartBase


class SessionCart(CartBase):
    """ Session based cart (Used with unauthorized users) """

    def __init__(self, request):
        # get session
        self.session = request.session

        # get cart dictionary
        if not self.session['cart']:
            self.session['cart'] = dict()
        self.cart = self.session['cart']

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







