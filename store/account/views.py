from django.shortcuts import render, redirect, Http404, reverse

from store.core.views import ShopViewBase

from .forms import RegistrationForm


class AccountView(ShopViewBase):
    name = 'Account'
    template_name = 'account/account.html'

    def prepare_context(self, request, *args, **kwargs):
        pass


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print('Form is valid')
            return redirect(reverse('index_page:index'))
        else:
            return render(request, 'account/register.html', {'form': RegistrationForm()})
    else:
        return render(request, 'account/register.html', {'form': RegistrationForm()})
