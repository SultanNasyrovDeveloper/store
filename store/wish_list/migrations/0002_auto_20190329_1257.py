# Generated by Django 2.1.7 on 2019-03-29 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wish_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wishlist',
            options={'verbose_name': 'wish list', 'verbose_name_plural': 'wish lists'},
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='items',
            field=models.ManyToManyField(null=True, to='catalog.Product', verbose_name='Products'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
