# Generated by Django 2.1.7 on 2019-03-29 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='img_alt',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Image alt text'),
        ),
    ]
