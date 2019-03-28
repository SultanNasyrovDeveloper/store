from django.db import models


class SiteSettings(models.Model):
    """ Site settings file """

    logo = models.FileField('Logo', upload_to='logo/', blank=True, null=True)
    logo_alt_text = models.CharField('Logo alt text', max_length=60, blank=True, null=True)

    class Meta:
        verbose_name = 'site settings'
        verbose_name_plural = 'site settings'

    def __str__(self):
        return 'Settings'
