# Generated by Django 2.1.7 on 2019-03-31 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index_page', '0003_banner_taglines'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'ordering': ('position',), 'verbose_name': 'banner', 'verbose_name_plural': 'banners'},
        ),
        migrations.AddField(
            model_name='banner',
            name='position',
            field=models.SmallIntegerField(default=1, verbose_name='Position'),
        ),
    ]
