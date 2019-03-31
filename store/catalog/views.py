from django.shortcuts import render

from store.core.views import ShopViewBase


class CatalogView(ShopViewBase):
    name = 'Catalog'
    template_name = 'catalog.html'

    def prepare_context(self):
        context = self.get_context()
