# Generated by Django 2.1.5 on 2019-09-21 17:43

from django.db import migrations


def init_data(apps, schema_editor):
    ContainerType = apps.get_model('boxes', 'ContainerType')
    ContainerType.objects.bulk_create([
        ContainerType(title='5-ти тонный'),
        ContainerType(title='3-х тонный'),
        ContainerType(title='20-и тонный'),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('boxes', '0006_auto_20190920_2126'),
    ]

    operations = [
        migrations.RunPython(init_data),
    ]
