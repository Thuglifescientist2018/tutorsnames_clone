# Generated by Django 3.2.6 on 2021-08-20 06:02

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20210820_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='select_country',
            field=django_countries.fields.CountryField(default='Select Countries', max_length=2),
        ),
    ]