# Generated by Django 2.1.7 on 2019-03-29 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wish_list', '0002_auto_20190329_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='items',
            field=models.ManyToManyField(blank=True, to='catalog.Product', verbose_name='Products'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='user',
            field=models.OneToOneField(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]