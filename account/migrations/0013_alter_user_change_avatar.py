# Generated by Django 3.2.6 on 2021-08-20 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_user_change_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='change_avatar',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
