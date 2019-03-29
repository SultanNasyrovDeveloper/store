from django.contrib import admin

from .models import WishList


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    pass
