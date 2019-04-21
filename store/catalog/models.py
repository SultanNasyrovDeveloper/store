from django.db import models
from django.urls import reverse

from mptt.models import MPTTModel, TreeForeignKey


class DisplayedProductsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(display=True)


class ProductBadge(models.Model):
    title = models.CharField('Title', max_length=15)
    icon = models.FileField('Icon', upload_to='badge_icons/', blank=True, null=True)

    class Meta:
        verbose_name = 'badge'
        verbose_name_plural = 'badges'

    def __str__(self):
        return self.title


class ProductCategory(MPTTModel):
    title = models.CharField('Title', max_length=30)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='subcategories',
                            related_query_name='subcategories', verbose_name='Parent')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # TODO implement
        pass


class ProductSize(models.Model):
    title = models.CharField('Title', max_length=100)

    class Meta:
        verbose_name = 'size'
        verbose_name_plural = 'sizes'

    def __str__(self):
        return self.title


class Product(models.Model):
    display = models.BooleanField('Display', default=True)

    title = models.CharField('Title', max_length=150, blank=True, null=True)
    badge = models.ForeignKey(ProductBadge, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Badge')
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, blank=True, null=True,
                                 verbose_name='Categories')
    size = models.ManyToManyField(ProductSize, blank=True, verbose_name='Size')

    # price
    price = models.SmallIntegerField('Price', blank=True, null=True)
    prev_price = models.SmallIntegerField('Previous price', blank=True, null=True)

    description = models.CharField(max_length=250, blank=True, null=True)
    creation_date = models.DateTimeField('Creation date', auto_now_add=True)

    objects = models.Manager()
    displayed = DisplayedProductsManager()

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '[ID={}] {}'.format(self.id, self.title or None)

    def get_absolute_url(self):
        return reverse('catalog:detail', kwargs={'product_id': str(self.id)})


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='images', related_query_name='images')
    file = models.FileField('File', upload_to='products/', blank=True, null=True)
    alt = models.CharField('Image alt text', max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'

    def __str__(self):
        return 'Product image {}'.format(self.id)



