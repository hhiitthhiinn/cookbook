# Generated by Django 4.0.6 on 2022-07-13 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0009_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigationmenu',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
