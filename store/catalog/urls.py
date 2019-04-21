from django.urls import path, include

from .views import CatalogView, ProductDetailView


app_name = 'catalog'


urlpatterns = [
    path('', CatalogView.as_view(), name='catalog'),
    path('detail/<int:product_id>', ProductDetailView.as_view(), name='detail'),
]