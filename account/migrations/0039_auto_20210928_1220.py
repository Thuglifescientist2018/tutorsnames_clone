# Generated by Django 3.2.6 on 2021-09-28 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0038_auto_20210928_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manageaddskills',
            name='skill_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='manageaddsubskills',
            name='sub_skill_status',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
