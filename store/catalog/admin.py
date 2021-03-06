from django.contrib import admin

from .models import Product, ProductSize, ProductImage, ProductCategory, ProductBadge


class ProductImageTabularAdmin(admin.TabularInline):
    model = ProductImage
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductImageTabularAdmin, )


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductBadge)
class ProductBadgeAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    pass
