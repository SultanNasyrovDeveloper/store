from django.shortcuts import render

from store.core.views import ShopViewBase


class CartView(ShopViewBase):
    name = 'Cart'
    template_name = 'cart/cart.html'

    def prepare_context(self, request, *args, **kwargs):
        pass
