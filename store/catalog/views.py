from django.shortcuts import render

from store.core.views import ShopViewBase
from store.catalog.filters import ProductFilter
from store.catalog.models import Product


class CatalogView(ShopViewBase):
    name = 'Catalog'
    template_name = 'catalog/catalog.html'

    def prepare_context(self, request):
        context = self.get_context()
        context['filter'] = ProductFilter(request.GET, queryset=Product.displayed.all())

