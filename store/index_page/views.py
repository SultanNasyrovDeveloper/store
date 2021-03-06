from django.shortcuts import render

from store.core.views import ShopViewBase

from store.catalog.models import Product

from .models import Banner


class IndexView(ShopViewBase):

    name = 'Index page'
    template_name = 'index_page/index.html'

    def get(self, request, *args, **kwargs):
        products = Product.displayed.all()
        context = self.get_context()
        context['banners'] = Banner.objects.all()
        context['new_products'] = products.order_by('creation_date')[:10]
        return render(request, self.template_name, context)
