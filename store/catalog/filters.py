import django_filters as filters

from .models import Product, ProductCategory


def categories(request):
    return


class ProductFilter(filters.FilterSet):

    class Meta:
        model = Product
        exclude = ('display', 'description',)
