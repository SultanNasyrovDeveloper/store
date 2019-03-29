from django.db import models


class ProductCategory(models.Model):
    title = models.CharField('Title', max_length=30)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='subcategories',
                               related_query_name='subcategories', verbose_name='Parent')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class ProductSize(models.Model):
    title = models.CharField('Title', max_length=100)

    class Meta:
        verbose_name = 'size'
        verbose_name_plural = 'sizes'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField('Title', max_length=150, blank=True, null=True)
    category = models.ManyToManyField(ProductCategory, blank=True, verbose_name='Categories')
    size = models.ForeignKey(ProductSize, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Size')

    # price
    price = models.SmallIntegerField('Price', blank=True, null=True)
    prev_price = models.SmallIntegerField('Previous price', blank=True, null=True)

    description = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '[ID={}] {}'.format(self.id, self.title or None)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file = models.FileField('File', upload_to='products/', blank=True, null=True)
    alt = models.CharField('Image alt text', max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'

    def __str__(self):
        return 'Product image {}'.format(self.id)



