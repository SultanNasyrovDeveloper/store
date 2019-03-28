from django.contrib import admin

from .models import SeoPage, Keyword


@admin.register(SeoPage)
class SeoPageAdmin(admin.ModelAdmin):
    fields = ('name', 'title', 'keywords', 'description')
    readonly_fields = ('name',)


@admin.register(Keyword)
class KeywordsAdmin(admin.ModelAdmin):
    pass
