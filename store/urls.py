from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('store.index_page.urls', namespace='index_page')),
    path('admin/', admin.site.urls),
    path('catalog/', include('store.catalog.urls', namespace='catalog')),
    path('cart/', include('store.cart.urls', namespace='cart')),
    path('account/', include('store.account.urls', namespace='account')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)