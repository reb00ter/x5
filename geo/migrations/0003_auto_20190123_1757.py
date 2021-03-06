# Generated by Django 2.1.5 on 2019-01-23 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0002_auto_20190123_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='geo.Region', verbose_name='регион'),
        ),
        migrations.AlterField(
            model_name='station',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='geo.City', verbose_name='город'),
        ),
    ]
