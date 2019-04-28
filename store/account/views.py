from django.shortcuts import render, redirect, Http404, reverse

from store.core.views import ShopViewBase

from .forms import RegistrationForm


class AccountView(ShopViewBase):
    name = 'Account'
    template_name = 'account/account.html'

    def prepare_context(self, request, *args, **kwargs):
        pass


def register(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('index_page:index'))
    return render(request, 'account/register.html', {'form': form})
