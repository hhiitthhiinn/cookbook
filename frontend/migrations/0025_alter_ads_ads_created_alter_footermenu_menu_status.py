# Generated by Django 4.0.6 on 2022-07-14 04:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0024_footermenu_alter_ads_ads_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='ads_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 14, 10, 19, 7, 94564), verbose_name='Ads Created Date'),
        ),
        migrations.AlterField(
            model_name='footermenu',
            name='menu_status',
            field=models.BooleanField(default=False, verbose_name='Disable'),
        ),
    ]