# Generated by Django 3.2.6 on 2021-08-20 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20210820_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='change_avatar',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]
