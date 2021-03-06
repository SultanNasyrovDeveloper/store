# Generated by Django 2.1.7 on 2019-03-31 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20190331_0127'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductBadge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15, verbose_name='Title')),
                ('icon', models.FileField(blank=True, null=True, upload_to='badge_icons/', verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'icon',
                'verbose_name_plural': 'icons',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='badge',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='catalog.ProductBadge', verbose_name='Badge'),
            preserve_default=False,
        ),
    ]
