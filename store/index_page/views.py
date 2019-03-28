from django.shortcuts import render

from store.core.views import ShopViewBase
from store.core.models import SiteSettings


class IndexView(ShopViewBase):

    name = 'Index page'
    template_name = 'index.html'

    def prepare_context(self):
        context = self.get_context()
        context['settings'], _ = SiteSettings.objects.get_or_create()
