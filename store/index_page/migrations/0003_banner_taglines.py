# Generated by Django 2.1.7 on 2019-03-31 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index_page', '0002_banner_img_alt'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='taglines',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Taglines html'),
        ),
    ]
