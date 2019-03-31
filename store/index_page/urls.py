from django.urls import path
from .views import IndexView


app_name = 'index_page'


urlpatterns = [
    path('', IndexView.as_view(), name='index')
]