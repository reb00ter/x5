# Generated by Django 2.1.5 on 2019-01-30 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searches', '0002_freecontainerrequest_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freecontainerrequest',
            name='location',
            field=models.ManyToManyField(blank=True, to='geo.Station', verbose_name='станции'),
        ),
        migrations.AlterField(
            model_name='freecontainerrequest',
            name='location_city',
            field=models.ManyToManyField(blank=True, to='geo.City', verbose_name='города'),
        ),
        migrations.AlterField(
            model_name='freecontainerrequest',
            name='location_city_region',
            field=models.ManyToManyField(blank=True, to='geo.Region', verbose_name='регионы'),
        ),
    ]