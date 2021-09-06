# Generated by Django 3.2.6 on 2021-08-25 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='appointment_boolean',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='contact_boolean',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='follow_unfollow_boolean',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_boolean',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='service_boolean',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='skill_boolean',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='testimonial_boolean',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
