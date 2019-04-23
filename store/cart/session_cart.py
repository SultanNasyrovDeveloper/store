from .base import CartBase


class SessionCartItem(object):
    def __init__(self):
        product = None
        self.dict_key = None
        self.name = product.name
        self.quantity = int()

    def serialize(self):
        pass


class SessionCart(CartBase):
    """ Session based cart (Used with unauthorized users) """

    def __init__(self, request):
        self.session = request.session
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

    def delete_item(self, item):
        """ Delete item from the cart """
        pass

    def clean_cart(self):
        """ Remove all items from the cart """
        pass

    def _save(self):
        """ Save cart to the session """
        self.session = self.cart







