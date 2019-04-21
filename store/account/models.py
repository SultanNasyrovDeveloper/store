from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account', related_query_name='account')
    first_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='First name')
    last_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Last name')
    phone_number = models.CharField(max_length=50, blank=True, null=True, verbose_name='Last name')
    creation_datetime = models.DateTimeField(auto_now=True, verbose_name='Creation date and time')

    class Meta:
        verbose_name = 'accounts'
        verbose_name_plural = 'accounts'

    def __str__(self):
        return self.first_name or 'Account {}'.format(self.id)

