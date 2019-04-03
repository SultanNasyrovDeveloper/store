from django.db import models


class Banner(models.Model):
    position = models.SmallIntegerField('Position', default=1)
    img = models.FileField('Image', upload_to='banners/', blank=True, null=True)
    img_alt = models.CharField('Image alt text', max_length=100, blank=True, null=True)

    # TODO change default field widget to TextField Widget
    taglines = models.CharField('Taglines html', max_length=300, blank=True, null=True)

    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'banners'
        ordering = ('position',)

    def __str__(self):
        return 'Banner {}'.format(self.position)


class PageSettings(models.Model):
    pass

