from django.db import models


class Keyword(models.Model):
    name = models.CharField('Name', max_length=25)

    class Meta:
        verbose_name = 'keyword'
        verbose_name_plural = 'keyword'

    def __str__(self):
        return self.name


class SeoPage(models.Model):
    name = models.CharField('Name', max_length=150, null=True, blank=True)
    title = models.CharField('Title', max_length=150, null=True, blank=True)
    keywords = models.ManyToManyField(Keyword, verbose_name='Keywords', blank=True)
    description = models.CharField('Description', max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = 'page'
        verbose_name_plural = 'pages'

    def __str__(self):
        return self.name

    @classmethod
    def optimize(cls, page_name):
        page_seo, _ = cls.objects.get_or_create(name=page_name)
        return page_seo
