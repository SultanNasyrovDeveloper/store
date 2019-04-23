from django.shortcuts import render, Http404

from store.core.views import ShopViewBase


class CartView(ShopViewBase):
    name = 'Cart'
    template_name = 'cart/cart.html'

    def prepare_context(self, request, *args, **kwargs):
        pass


def add_item(request):
    if request.method == 'POST' and request.is_ajax():
        pass
    else:
        raise Http404


def delete_item(request):
    if request.method == 'POST' and request.is_ajax():
        pass
    else:
        raise Http404


def change_quantity(request):
    if request.method == 'POST' and request.is_ajax():
        pass
    else:
        raise Http404


def clean_cart(request):
    if request.method == 'POST' and request.is_ajax():
        pass
    else:
        raise Http404





