# Generated by Django 3.2.6 on 2021-08-20 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_remove_user_change_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='change_avatar',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/'),
        ),
    ]
