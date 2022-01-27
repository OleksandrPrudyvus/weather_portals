# Generated by Django 4.0.1 on 2022-01-27 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0005_rename_store_city_story'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='story',
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='feels_like',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='icon',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='temp',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='temp_max',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='temp_min',
            field=models.FloatField(null=True),
        ),
    ]
