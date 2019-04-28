from django.shortcuts import render

from store.core.views import ShopViewBase
from store.catalog.filters import ProductFilter
from store.catalog.models import Product


class CatalogView(ShopViewBase):
    name = 'Catalog'
    template_name = 'catalog/catalog.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context()
        context['products'] = Product.displayed.all()
        context['filter'] = ProductFilter(request.GET, queryset=Product.displayed.all())
        return render(request, self.template_name, context)


class ProductDetailView(ShopViewBase):
    name = 'Product Detail'
    template_name = 'catalog/detail.html'

    def get(self, request, *args, **kwargs):
        """ Product detail view """
        context = self.get_context()
        # TODO Поправить распаковку аргументов. Сейчас не очень правильно достаются агрументы
        product_id = args[1].get('product_id')
        context['product'] = Product.displayed.get(id=int(product_id))
        return render(request, self.template_name, context)

