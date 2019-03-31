from django.db import models


class Banner(models.Model):
    img = models.FileField('Image', upload_to='banners/', blank=True, null=True)
    img_alt = models.CharField('Image alt text', max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'banners'

    def __str__(self):
        return 'Banner {}'.format(self.id)

