# Generated by Django 4.0.6 on 2022-07-14 03:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0018_alter_ads_ads_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='ads_image',
            field=models.ImageField(default=datetime.datetime(2022, 7, 14, 3, 54, 42, 950264, tzinfo=utc), upload_to='ads', verbose_name='Ads Image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ads',
            name='ads_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 14, 9, 23, 34, 64668), verbose_name='Ads Created Date'),
        ),
    ]
