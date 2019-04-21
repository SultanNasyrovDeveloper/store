from django.shortcuts import render
from django.views.generic import View

from store.seo.models import SeoPage


class ShopViewBase(View):
    """ Shop Base View"""

    name = None
    template_name = None

    def __init__(self):
        super().__init__()
        self._context = {}

    def get_context(self):
        return self._context

    def prepare_seo(self):
        context = self.get_context()
        context['seo'] = SeoPage.optimize(self.name)

    def prepare_context(self, request, *args, **kwargs):
        return NotImplementedError

    def get(self, request, *args, **kwargs):
        self.prepare_seo()
        self.prepare_context(request, args, kwargs)
        context = self.get_context()
        return render(request, self.template_name, context)
