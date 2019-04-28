from django.urls import path

from .views import AccountView, register

app_name = 'account'


urlpatterns = [
    path('', AccountView.as_view(), name='account_page'),
    path('register', register, name='register')
]