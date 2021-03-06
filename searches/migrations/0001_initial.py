# Generated by Django 2.1.5 on 2019-01-29 22:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('geo', '0003_auto_20190123_1757'),
        ('boxes', '0003_auto_20190123_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreeContainerRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField(blank=True, null=True, verbose_name='с')),
                ('date_till', models.DateField(blank=True, null=True, verbose_name='по')),
                ('count', models.PositiveIntegerField(default=1, verbose_name='количество')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='адрес')),
                ('created', models.DateField(auto_now_add=True, verbose_name='создан')),
                ('location', models.ManyToManyField(to='geo.Station', verbose_name='станции')),
                ('location_city', models.ManyToManyField(to='geo.City', verbose_name='города')),
                ('location_city_region', models.ManyToManyField(to='geo.Region', verbose_name='регионы')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boxes.ContainerType', verbose_name='тип контейнера')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
