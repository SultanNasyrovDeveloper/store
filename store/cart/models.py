from django.db import models
from django.contrib.auth

from .cart import CartBase


class DatabaseCart(models.Model, CartBase):
    pass


