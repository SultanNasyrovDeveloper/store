from django.shortcuts import render

from store.core.views import ShopViewBase


class IndexView(ShopViewBase):

    name = 'Index page'
    template_name = 'index.html'

    def prepare_context(self):
        pass
