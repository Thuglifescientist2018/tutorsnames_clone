# Generated by Django 3.2.6 on 2021-08-17 03:39

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_updateinfo_agree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updateinfo',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='updateinfo',
            name='email',
            field=models.EmailField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='updateinfo',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='updateinfo',
            name='password',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='updateinfo',
            name='username',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
