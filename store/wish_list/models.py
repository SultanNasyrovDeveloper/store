from django.db import models
from django.contrib.auth.models import User


class WishList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    items = models.ManyToManyField('catalog.Product', blank=True, verbose_name='Products')

    class Meta:
        verbose_name = 'wish list'
        verbose_name_plural = 'wish lists'

    def __str__(self):
        return 'Wish List {}, user {}'.format(self.id, self.user.username)
