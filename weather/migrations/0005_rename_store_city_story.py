# Generated by Django 4.0.1 on 2022-01-21 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0004_city_data_city_store'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='store',
            new_name='story',
        ),
    ]