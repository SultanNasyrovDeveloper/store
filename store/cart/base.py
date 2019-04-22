

class CartItemBase(object):
    pass


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

    def add_item(self, item):
        return NotImplementedError

    def remove_item(self, item):
        return NotImplementedError

    def change_quantity(self, item):
        return NotImplementedError

    def clean_cart(self):
        return NotImplementedError
