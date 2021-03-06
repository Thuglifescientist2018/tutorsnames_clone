# Generated by Django 3.2.6 on 2021-08-20 15:32

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_rename_your_name_user_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about_me',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='designation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
