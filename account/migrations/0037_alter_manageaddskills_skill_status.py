# Generated by Django 3.2.6 on 2021-09-27 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0036_alter_manageaddsubskills_sub_skill_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manageaddskills',
            name='skill_status',
            field=models.BooleanField(default=True),
        ),
    ]
