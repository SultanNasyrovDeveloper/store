# Generated by Django 2.1.7 on 2019-04-21 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_auto_20190331_0241'),
        ('wish_list', '0004_remove_wishlist_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='products',
            field=models.ManyToManyField(blank=True, to='catalog.Product', verbose_name='Products'),
        ),
    ]
