# Generated by Django 4.0.6 on 2022-07-14 04:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0023_bloginfo_alter_ads_ads_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_title', models.CharField(max_length=100, verbose_name='title')),
                ('menu_link', models.CharField(max_length=100, verbose_name='link')),
                ('menu_status', models.BooleanField(default=True, verbose_name='Disable')),
            ],
        ),
        migrations.AlterField(
            model_name='ads',
            name='ads_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 14, 10, 18, 15, 803548), verbose_name='Ads Created Date'),
        ),
    ]
